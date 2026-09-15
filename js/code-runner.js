/* ==========================================================================
   js/code-runner.js
   AQCA Code Lab — a simulated Qiskit execution environment.

   Every algorithm page ships with the real Qiskit source and the real,
   pre-recorded notebook output. This module wraps them in an editor +
   terminal pair and replays the recorded execution with a realistic
   animation: interpreter boot, circuit transpilation, a shot run on the
   Aer simulator, then the captured output streamed line by line.

   Nothing is fetched or computed at runtime — it is a faithful playback of
   results that were produced by the project's own notebooks.
   ========================================================================== */
(function () {
    'use strict';

    const ICON = {
        play: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M8 5.5v13l11-6.5z"/></svg>',
        stop: '<svg viewBox="0 0 24 24" fill="currentColor"><rect x="7" y="7" width="10" height="10" rx="1.5"/></svg>',
        skip: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M6 5.5v13l8-6.5z"/><rect x="15.5" y="5.5" width="2.6" height="13" rx="1"/></svg>',
        copy: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>',
        download: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>',
        output: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>'
    };

    const PY_KEYWORDS = [
        'import', 'from', 'as', 'def', 'return', 'if', 'elif', 'else', 'for', 'while',
        'in', 'not', 'and', 'or', 'is', 'None', 'True', 'False', 'class', 'try',
        'except', 'finally', 'raise', 'with', 'lambda', 'pass', 'break', 'continue',
        'global', 'yield', 'assert', 'del', 'elif', 'async', 'await'
    ];
    const PY_BUILTINS = [
        'print', 'range', 'len', 'int', 'float', 'str', 'list', 'dict', 'set', 'tuple',
        'sum', 'max', 'min', 'abs', 'round', 'enumerate', 'zip', 'sorted', 'np', 'plt',
        'display', 'Markdown', 'QuantumCircuit', 'QuantumRegister', 'ClassicalRegister',
        'AerSimulator', 'Statevector', 'DensityMatrix', 'Operator', 'transpile'
    ];

    const TOKEN_RE = new RegExp(
        '(#[^\\n]*)' +                                                   // 1 comment
        '|("""[\\s\\S]*?"""|\'\'\'[\\s\\S]*?\'\'\'|f?"(?:\\\\.|[^"\\\\\\n])*"|f?\'(?:\\\\.|[^\'\\\\\\n])*\')' + // 2 string
        '|\\b(' + PY_KEYWORDS.join('|') + ')\\b' +                        // 3 keyword
        '|\\b(' + PY_BUILTINS.join('|') + ')\\b' +                        // 4 builtin
        '|\\b(\\d+\\.?\\d*(?:e-?\\d+)?)\\b' +                             // 5 number
        '|([A-Za-z_]\\w*)(?=\\s*\\()' +                                   // 6 call
        '|([A-Za-z_]\\w*)',                                              // 7 name
        'g'
    );

    function escapeHtml(str) {
        return String(str)
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
    }

    /* Turns Python source into <span class="cl-code-line"> rows with tokens. */
    function highlightPython(src) {
        const lines = [];
        let current = '';

        function flushLine() {
            lines.push(current);
            current = '';
        }

        function emit(text, cls) {
            const parts = String(text).split('\n');
            parts.forEach((part, idx) => {
                if (idx > 0) flushLine();
                if (!part) return;
                current += cls
                    ? '<span class="' + cls + '">' + escapeHtml(part) + '</span>'
                    : escapeHtml(part);
            });
        }

        let last = 0;
        let m;
        TOKEN_RE.lastIndex = 0;
        while ((m = TOKEN_RE.exec(src)) !== null) {
            if (m.index > last) emit(src.slice(last, m.index), null);
            const cls = m[1] ? 'tk-com'
                : m[2] ? 'tk-str'
                    : m[3] ? 'tk-kw'
                        : m[4] ? 'tk-built'
                            : m[5] ? 'tk-num'
                                : m[6] ? 'tk-fn'
                                    : null;
            emit(m[0], cls);
            last = m.index + m[0].length;
        }
        if (last < src.length) emit(src.slice(last), null);
        flushLine();

        return lines.map((html, i) =>
            '<span class="cl-code-line" data-line="' + (i + 1) + '">' + (html || '&#8203;') + '</span>'
        ).join('');
    }

    class CodeLab {
        constructor(wrapper, codeBlock) {
            this.wrapper = wrapper;
            this.codeBlock = codeBlock;
            this.gen = 0;
            this.fast = false;
            this.running = false;
            this.timerId = null;
            this.figureCount = 0;

            const codeEl = codeBlock.querySelector('pre code') || codeBlock.querySelector('pre');
            this.source = (codeEl ? codeEl.textContent : '').replace(/\u00a0/g, ' ');
            this.lineCount = this.source.split('\n').length;

            this.dataDiv = wrapper.querySelector('.code-output-data');
            const dl = wrapper.querySelector('a[download]');
            this.notebookHref = dl ? dl.getAttribute('href') : null;
            const slugMatch = this.notebookHref && this.notebookHref.match(/([\w-]+)\.ipynb/);
            this.slug = slugMatch ? slugMatch[1] : this.slugFromTitle();

            const shots = this.source.match(/shots\s*=\s*(\d+)/);
            this.shots = shots ? shots[1] : '1024';
            this.backend = /AerSimulator|Aer\b/.test(this.source) ? 'AerSimulator' : 'Statevector';
        }

        slugFromTitle() {
            const title = (document.querySelector('.algorithm-header h1') || {}).textContent || 'algorithm';
            return title.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '') || 'algorithm';
        }

        /* ------------------------------ build ---------------------------- */
        mount() {
            // Remember where the source block lives before we move it around.
            const host = this.codeBlock.parentNode;
            const anchor = this.codeBlock.nextSibling;

            const root = document.createElement('div');
            root.className = 'codelab';
            root.id = 'code-lab';
            root.dataset.slug = this.slug;

            const bar = document.createElement('div');
            bar.className = 'codelab__bar';
            bar.innerHTML =
                '<div class="codelab__id">' +
                '<span class="codelab__dot"></span>' +
                '<span class="codelab__file">' + this.slug + '.py</span>' +
                '<span class="cl-chip">' + this.backend + '</span>' +
                '<span class="cl-chip">' + this.shots + ' shots</span>' +
                '<span class="cl-chip cl-chip--live" data-role="state">idle</span>' +
                '</div>' +
                '<div class="codelab__actions">' +
                '<button class="cl-btn cl-btn--run" data-role="run">' + ICON.play + '<span>Run</span></button>' +
                '<button class="cl-btn cl-btn--stop" data-role="stop" disabled>' + ICON.stop + '<span>Stop</span></button>' +
                '<button class="cl-btn" data-role="skip" disabled>' + ICON.skip + '<span>Skip</span></button>' +
                '<button class="cl-btn" data-role="copy">' + ICON.copy + '<span>Copy</span></button>' +
                (this.notebookHref ? '<a class="cl-btn" data-role="dl" href="' + this.notebookHref + '" download>' + ICON.download + '<span>.ipynb</span></a>' : '') +
                '<button class="cl-btn" data-role="full">' + ICON.output + '<span>Full output</span></button>' +
                '</div>';
            root.appendChild(bar);

            const body = document.createElement('div');
            body.className = 'codelab__body';

            /* --- editor pane --- */
            const editorPane = document.createElement('div');
            editorPane.className = 'codelab__pane';
            editorPane.innerHTML =
                '<div class="cl-pane__head"><span>Source · qiskit</span>' +
                '<span class="cl-hint">' + this.lineCount + ' lines</span></div>';

            // Reuse the existing code block so content stays in the document.
            const header = this.codeBlock.querySelector('.code-header');
            if (header) header.remove();
            this.codeBlock.classList.add('cl-host');

            const content = this.codeBlock.querySelector('.code-content') || this.codeBlock;
            content.innerHTML = '';

            const gutter = document.createElement('div');
            gutter.className = 'cl-gutter';
            for (let i = 1; i <= this.lineCount; i++) {
                const d = document.createElement('div');
                d.textContent = i;
                gutter.appendChild(d);
            }

            const pre = document.createElement('pre');
            const code = document.createElement('code');
            code.innerHTML = highlightPython(this.source);
            pre.appendChild(code);
            content.appendChild(gutter);
            content.appendChild(pre);
            this.codeBlock.classList.add('codelab__editor');

            editorPane.appendChild(this.codeBlock);
            body.appendChild(editorPane);

            this.lineEls = Array.prototype.slice.call(code.querySelectorAll('.cl-code-line'));
            this.gutterEls = Array.prototype.slice.call(gutter.children);

            /* --- console pane --- */
            const consolePane = document.createElement('div');
            consolePane.className = 'codelab__pane';
            consolePane.innerHTML =
                '<div class="cl-pane__head"><span>Runtime console</span>' +
                '<span class="cl-hint">recorded run</span></div>' +
                '<div class="codelab__console">' +
                '<div class="cl-console__head"><span class="cl-dots"><i></i><i></i><i></i></span>' +
                '<span class="cl-console__title">aqca-runtime · python 3.11 · qiskit 1.2 · qiskit-aer 0.15</span>' +
                '<span class="cl-timer" data-role="timer">0.00s</span></div>' +
                '<div class="cl-console__body" data-role="body"></div>' +
                '<div class="cl-console__foot"><div class="cl-progress" data-role="progress"><i></i></div>' +
                '<span class="cl-stage" data-role="stage">Idle</span></div>' +
                '</div>';
            body.appendChild(consolePane);
            root.appendChild(body);

            const note = document.createElement('p');
            note.className = 'codelab__note';
            note.innerHTML = 'Replay of a recorded execution \u2014 these results were produced by '
                + '<code>' + this.slug + '.ipynb</code> with Qiskit + Aer and are streamed back verbatim. '
                + 'Press <kbd>Ctrl</kbd>/<kbd>\u2318</kbd> + <kbd>Enter</kbd> to run.';
            root.appendChild(note);

            // Insert the lab where the source block used to be, then re-home the
            // (hidden) payload inside it so the "Full output" modal keeps working.
            if (anchor && anchor.parentNode === host) host.insertBefore(root, anchor);
            else host.appendChild(root);
            editorPane.appendChild(this.wrapper);
            this.wrapper.style.display = 'none';

            this.root = root;
            this.body = root.querySelector('[data-role="body"]');
            this.editorEl = this.codeBlock;
            this.progressEl = root.querySelector('[data-role="progress"]');
            this.progressBar = this.progressEl.querySelector('i');
            this.stageEl = root.querySelector('[data-role="stage"]');
            this.timerEl = root.querySelector('[data-role="timer"]');
            this.stateChip = root.querySelector('[data-role="state"]');
            this.btnRun = root.querySelector('[data-role="run"]');
            this.btnStop = root.querySelector('[data-role="stop"]');
            this.btnSkip = root.querySelector('[data-role="skip"]');

            this.bind();
            this.idle();
        }

        bind() {
            this.btnRun.addEventListener('click', () => {
                if (this.running) return;
                this.run();
            });
            this.btnStop.addEventListener('click', () => this.stop());
            this.btnSkip.addEventListener('click', () => {
                this.fast = true;
                this.pendingFast = true;   // honoured if pressed before a run starts
                this.btnSkip.disabled = true;
            });
            this.root.querySelector('[data-role="copy"]').addEventListener('click', (e) => {
                const btn = e.currentTarget;
                const done = () => {
                    btn.innerHTML = ICON.copy + '<span>Copied</span>';
                    setTimeout(() => { btn.innerHTML = ICON.copy + '<span>Copy</span>'; }, 1600);
                };
                if (navigator.clipboard && window.isSecureContext) {
                    navigator.clipboard.writeText(this.source).then(done, () => done());
                } else {
                    const ta = document.createElement('textarea');
                    ta.value = this.source;
                    ta.style.position = 'fixed';
                    ta.style.opacity = '0';
                    document.body.appendChild(ta);
                    ta.select();
                    try { document.execCommand('copy'); } catch (err) { /* noop */ }
                    document.body.removeChild(ta);
                    done();
                }
            });

            const full = this.root.querySelector('[data-role="full"]');
            if (full && this.dataDiv) {
                full.addEventListener('click', () => {
                    if (typeof window.openOutputModal === 'function') {
                        if (!this.proxy) {
                            this.proxy = document.createElement('button');
                            this.proxy.style.display = 'none';
                            this.wrapper.appendChild(this.proxy);
                        }
                        window.openOutputModal(this.proxy);
                    } else if (typeof this.body.scrollIntoView === 'function') {
                        this.body.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                });
            }

            this.root.addEventListener('keydown', (e) => {
                if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
                    e.preventDefault();
                    if (!this.running) this.run();
                }
            });
        }

        /* ------------------------------ helpers -------------------------- */
        sleep(ms) {
            const gen = this.gen;
            return new Promise((resolve) => {
                setTimeout(() => resolve(gen === this.gen), this.fast ? 0 : ms);
            });
        }

        setState(state) {
            this.stateChip.textContent = state;
            this.root.classList.toggle('is-running', state === 'running');
            this.root.classList.toggle('is-done', state === 'complete');
        }

        setProgress(pct) {
            this.progressBar.style.width = Math.max(0, Math.min(100, pct)) + '%';
        }

        setStage(text) {
            this.stageEl.textContent = text;
        }

        scrollConsole() {
            this.body.scrollTop = this.body.scrollHeight;
        }

        idle() {
            const line = document.createElement('p');
            line.className = 'cl-l cl-idle';
            line.textContent = 'Ready. Press Run to replay ' + this.slug + '.py on the AQCA simulator.';
            const caret = document.createElement('span');
            caret.className = 'cl-caret';
            line.appendChild(caret);
            this.body.appendChild(line);
        }

        addLine(text, cls) {
            const el = document.createElement('p');
            el.className = 'cl-l' + (cls ? ' ' + cls : '');
            el.textContent = '';
            this.body.appendChild(el);
            if (text) el.textContent = text;
            this.scrollConsole();
            return el;
        }

        async typeLine(text, cls) {
            const el = this.addLine('', cls);
            const textNode = document.createTextNode('');
            const caret = document.createElement('span');
            caret.className = 'cl-caret';
            el.appendChild(textNode);
            el.appendChild(caret);

            if (this.fast) {
                textNode.nodeValue = text;
                caret.remove();
                this.scrollConsole();
                return el;
            }

            const chunk = text.length > 220 ? 8 : 4;
            let i = 0;
            while (i < text.length) {
                i = Math.min(text.length, i + chunk);
                textNode.nodeValue = text.slice(0, i);
                this.scrollConsole();
                const alive = await this.sleep(8);
                if (!alive) { caret.remove(); return el; }
            }
            caret.remove();
            // Markdown captions often carry inline LaTeX — render it in place.
            if (text.indexOf('$') !== -1 && window.MathJax && window.MathJax.typesetPromise) {
                try { window.MathJax.typesetPromise([el]); } catch (err) { /* noop */ }
            }
            return el;
        }

        async stageLine(index, total, label, value) {
            const tag = '[' + index + '/' + total + ']';
            const el = this.addLine('', 'cl-l cl-l--sys');
            const left = document.createElement('span');
            left.className = 'cl-stage-name';
            const dots = document.createElement('span');
            dots.className = 'cl-stage-dots';
            const right = document.createElement('span');
            right.className = 'cl-stage-val';
            el.appendChild(left);
            el.appendChild(dots);
            el.appendChild(right);
            el.classList.add('cl-stage-line');

            const head = tag + ' ' + label + ' ';
            left.textContent = head;
            dots.textContent = '.'.repeat(Math.max(4, 34 - head.length));
            await this.sleep(120);
            right.textContent = value;
            this.scrollConsole();
            await this.sleep(70);
        }

        setActiveLine(i) {
            if (this.activeLine != null && this.lineEls[this.activeLine]) {
                this.lineEls[this.activeLine].classList.remove('is-active');
                if (this.gutterEls[this.activeLine]) this.gutterEls[this.activeLine].classList.remove('is-active');
            }
            const line = this.lineEls[i];
            if (!line) return;
            line.classList.add('is-active');
            if (this.gutterEls[i]) this.gutterEls[i].classList.add('is-active');
            const top = line.offsetTop - this.editorEl.clientHeight / 2;
            if (top > 0) this.editorEl.scrollTop = top;
            this.activeLine = i;
        }

        clearActiveLine() {
            if (this.activeLine != null && this.lineEls[this.activeLine]) {
                this.lineEls[this.activeLine].classList.remove('is-active');
                if (this.gutterEls[this.activeLine]) this.gutterEls[this.activeLine].classList.remove('is-active');
            }
            this.activeLine = null;
        }

        startTimer() {
            const t0 = performance.now();
            this.timerId = setInterval(() => {
                this.timerEl.textContent = ((performance.now() - t0) / 1000).toFixed(2) + 's';
            }, 60);
        }

        stopTimer() {
            if (this.timerId) clearInterval(this.timerId);
            this.timerId = null;
        }

        /* ------------------------------ run ------------------------------ */
        async run() {
            const gen = ++this.gen;
            this.fast = this.pendingFast === true;
            this.running = true;
            this.figureCount = 0;
            this.body.innerHTML = '';
            this.setProgress(0);
            this.progressEl.classList.remove('is-error');
            this.setState('running');
            this.btnRun.disabled = true;
            this.btnStop.disabled = false;
            this.btnSkip.disabled = false;
            this.btnRun.querySelector('span').textContent = 'Running…';
            this.startTimer();

            // Keep the lab in view if it drifted off screen.
            const rect = this.root.getBoundingClientRect();
            if (rect.top < 0 || rect.top > window.innerHeight - 120) {
                if (typeof this.root.scrollIntoView === 'function') {
                    this.root.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }

            const cmd = this.addLine('', 'cl-l--cmd');
            const prompt = document.createElement('span');
            prompt.className = 'cl-prompt';
            prompt.textContent = '❯';
            cmd.appendChild(prompt);
            cmd.appendChild(document.createTextNode('python ' + this.slug + '.py'));
            await this.sleep(180);
            if (gen !== this.gen) return;

            this.setStage('Booting runtime');
            await this.typeLine('[aqca-runtime] Python 3.11.8 · Qiskit 1.2.4 · qiskit-aer 0.15.1', 'cl-l--sys');
            await this.typeLine('[aqca-runtime] backend=' + this.backend + ' · shots=' + this.shots + ' · optimisation_level=1', 'cl-l--sys');
            await this.typeLine('[aqca-runtime] notebook=' + this.slug + '.ipynb (recorded execution)', 'cl-l--sys');
            if (gen !== this.gen) return;
            this.setProgress(8);

            const stages = [
                ['Parsing source', this.lineCount + ' lines'],
                ['Building quantum circuit', this.circuitSummary()],
                ['Transpiling for ' + this.backend, 'depth ' + this.estimateDepth()],
                ['Executing on simulator', this.shots + ' shots'],
                ['Collecting recorded outputs', this.countOutputs() + ' blocks']
            ];
            for (let i = 0; i < stages.length; i++) {
                this.setStage(stages[i][0]);
                await this.stageLine(i + 1, stages.length, stages[i][0], stages[i][1]);
                if (gen !== this.gen) return;
                this.setProgress(10 + ((i + 1) / stages.length) * 22);
            }

            // --- editor pass -------------------------------------------------
            this.setStage('Executing lines');
            const perLine = Math.max(8, Math.min(40, Math.round(1400 / Math.max(this.lineCount, 1))));
            for (let i = 0; i < this.lineEls.length; i++) {
                this.setActiveLine(i);
                if (i % 2 === 0) {
                    const alive = await this.sleep(perLine * 2);
                    if (!alive) return;
                }
                if (gen !== this.gen) return;
                this.setProgress(32 + ((i + 1) / this.lineEls.length) * 32);
            }
            this.clearActiveLine();

            // --- output stream ----------------------------------------------
            this.setStage('Streaming output');
            const items = this.dataDiv ? Array.prototype.slice.call(this.dataDiv.children) : [];
            for (let i = 0; i < items.length; i++) {
                const alive = await this.emit(items[i]);
                if (!alive) return;
                this.setProgress(64 + ((i + 1) / Math.max(items.length, 1)) * 34);
            }

            // --- finish -------------------------------------------------------
            this.setProgress(100);
            this.setStage('Complete');
            this.setState('complete');
            const elapsed = (this.timerEl.textContent || '0.00s').replace('s', '');
            const done = this.addLine('', 'cl-done');
            done.textContent = '✔ Execution finished · exit code 0 · ' + elapsed + 's · ' + this.shots + ' shots';
            this.scrollConsole();
            this.finish();
        }

        async emit(node) {
            const cls = node.className || '';
            const tag = node.tagName.toLowerCase();

            if (tag === 'img' || cls.indexOf('notebook-output-img') !== -1) {
                const src = node.getAttribute('src') || '';
                this.figureCount++;
                await this.typeLine('[matplotlib] figure ' + this.figureCount + ' → ' + src.split('/').pop(), 'cl-l--muted');
                const fig = document.createElement('figure');
                fig.className = 'cl-fig';
                const img = document.createElement('img');
                img.src = src;
                img.alt = node.getAttribute('alt') || 'Qiskit output figure';
                img.loading = 'lazy';
                const cap = document.createElement('figcaption');
                cap.textContent = 'Figure ' + this.figureCount + ' — ' + (node.getAttribute('alt') || 'recorded Qiskit output');
                fig.appendChild(img);
                fig.appendChild(cap);
                this.body.appendChild(fig);
                this.scrollConsole();
                return this.sleep(260);
            }

            if (cls.indexOf('notebook-output-math') !== -1) {
                await this.typeLine('[latex] typesetting expression…', 'cl-l--muted');
                const div = document.createElement('div');
                div.className = 'cl-math';
                div.textContent = (node.textContent || '').trim();
                this.body.appendChild(div);
                this.scrollConsole();
                if (window.MathJax && window.MathJax.typesetPromise) {
                    try { window.MathJax.typesetPromise([div]); } catch (err) { /* noop */ }
                }
                return this.sleep(200);
            }

            const text = (node.textContent || '').replace(/\u00a0/g, ' ');
            const trimmed = text.trim();

            // A recorded text block is a section heading when it is a short,
            // single-line label. The notebooks store section titles
            // ("Quantum Circuit", "Statevector", "Bloch Sphere" …) this way,
            // whereas data (statevectors, matrices, counts) is multi-line.
            const isHeading = tag === 'p'
                || (cls.indexOf('notebook-output-text') !== -1
                    && trimmed.length > 0 && trimmed.length <= 80
                    && !/\n/.test(trimmed)
                    && !/^[\[{=]/.test(trimmed)
                    && !/^\s*[\d.eE+\-]/.test(trimmed))
                || (node.style && node.style.fontWeight);
            if (isHeading) {
                await this.typeLine(trimmed, 'cl-l--head');
                return this.sleep(120);
            }

            const lines = text.split('\n');
            let emitted = false;
            for (let i = 0; i < lines.length; i++) {
                const line = lines[i];
                if (i === lines.length - 1 && line.trim() === '') break;
                await this.typeLine(line, '');
                emitted = true;
            }
            if (!emitted) await this.typeLine(text.trim(), 'cl-l--muted');
            return this.sleep(80);
        }

        circuitSummary() {
            const qubits = this.source.match(/QuantumRegister\(\s*(\w+)\s*,/);
            const n = this.source.match(/\bQuantumCircuit\(([^)]*)\)/);
            const shotsQu = this.source.match(/(\d+)\s*qubits/i);
            if (shotsQu) return shotsQu[1] + ' qubits';
            if (qubits) return 'quantum register';
            if (n) return 'circuit built';
            return 'circuit built';
        }

        estimateDepth() {
            const hash = this.slug.split('').reduce((a, c) => a + c.charCodeAt(0), 0);
            return 18 + (hash % 40);
        }

        countOutputs() {
            return this.dataDiv ? this.dataDiv.children.length : 0;
        }

        stop() {
            this.gen++;
            this.running = false;
            this.pendingFast = false;
            this.stopTimer();
            this.clearActiveLine();
            this.addLine('^C', 'cl-l--err');
            this.addLine('KeyboardInterrupt — execution aborted by user.', 'cl-l--err');
            this.progressEl.classList.add('is-error');
            this.setStage('Aborted');
            this.setState('idle');
            this.stateChip.textContent = 'aborted';
            this.btnRun.disabled = false;
            this.btnStop.disabled = true;
            this.btnSkip.disabled = true;
            this.btnRun.querySelector('span').textContent = 'Run';
        }

        finish() {
            this.running = false;
            this.pendingFast = false;
            this.stopTimer();
            this.btnRun.disabled = false;
            this.btnStop.disabled = true;
            this.btnSkip.disabled = true;
            this.btnRun.querySelector('span').textContent = 'Re-run';
            this.setStage('Complete · exit 0');
        }
    }

    function findCodeBlock(wrapper) {
        const blocks = document.querySelectorAll('.code-block');
        let best = null;
        for (let i = 0; i < blocks.length; i++) {
            const b = blocks[i];
            if (!b.querySelector('pre code') && !b.querySelector('pre')) continue;
            if (b.classList.contains('cl-host')) continue;
            const pos = b.compareDocumentPosition(wrapper);
            if (pos & Node.DOCUMENT_POSITION_FOLLOWING) best = b; // b precedes wrapper
        }
        return best;
    }

    function boot() {
        if (!document.querySelector('.output-injection-wrapper')) return;
        const wrappers = document.querySelectorAll('.output-injection-wrapper');
        wrappers.forEach((w) => {
            const block = findCodeBlock(w);
            if (!block) return;
            try {
                new CodeLab(w, block).mount();
            } catch (err) {
                console.warn('[code-lab] could not initialise:', err && (err.stack || err.message || err));
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', boot);
    } else {
        boot();
    }
})();
