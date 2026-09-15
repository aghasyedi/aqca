/* ==========================================================================
   js/quantum-core.js
   Shared quantum simulation engine for the AQCA interactive visualisers.

   Exposes one global:  QC
     QC.C / cadd / csub / cmul / cscl / cconj / cabs / carg / cexp / cdiv
     QC.GATES                  - named 2x2 gate matrices
     QC.Rx / Ry / Rz / P / U3  - parameterised 2x2 gates
     QC.zeroState / apply1q / applyCtrl / apply2q / cnot / cz / swap
     QC.probs / sample / sampleMany / bloch / expect
     QC.entanglement            - concurrence + entropy of a 2 qubit state
     QC.gatePow(U, t)           - principal matrix power, used for animation
     QC.Bloch                   - canvas Bloch sphere renderer
     QC.fmt / QC.polar / QC.labels / QC.snap / QC.deg

   Qubit convention: qubit q0 is the LEFT-most (most significant) bit, so
   |q0 q1> = |00>, |01>, |10>, |11> map to indices 0,1,2,3.
   ========================================================================== */
(function (global) {
    'use strict';

    /* ------------------------------------------------------------------ *
     * 1. Complex arithmetic                                              *
     * ------------------------------------------------------------------ */
    function C(re, im) {
        return { re: re === undefined ? 0 : re, im: im === undefined ? 0 : im };
    }
    function cadd(a, b) { return C(a.re + b.re, a.im + b.im); }
    function csub(a, b) { return C(a.re - b.re, a.im - b.im); }
    function cmul(a, b) { return C(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re); }
    function cscl(a, s) { return C(a.re * s, a.im * s); }
    function cconj(a) { return C(a.re, -a.im); }
    function cabs(a) { return Math.sqrt(a.re * a.re + a.im * a.im); }
    function carg(a) { return Math.atan2(a.im, a.re); }
    function cexp(t) { return C(Math.cos(t), Math.sin(t)); }
    function cdiv(a, b) {
        var d = b.re * b.re + b.im * b.im;
        if (d === 0) return C(0, 0);
        return C((a.re * b.re + a.im * b.im) / d, (a.im * b.re - a.re * b.im) / d);
    }
    var EPS = 1e-12;
    function snap(a, eps) {
        eps = eps === undefined ? 1e-10 : eps;
        return C(Math.abs(a.re) < eps ? 0 : a.re, Math.abs(a.im) < eps ? 0 : a.im);
    }

    /* ------------------------------------------------------------------ *
     * 2. Gate library (2x2, arrays of complex)                           *
     * ------------------------------------------------------------------ */
    var S2 = 1 / Math.SQRT2;

    var GATES = {
        I: [[C(1), C(0)], [C(0), C(1)]],
        X: [[C(0), C(1)], [C(1), C(0)]],
        Y: [[C(0), C(0, -1)], [C(0, 1), C(0)]],
        Z: [[C(1), C(0)], [C(0), C(-1)]],
        H: [[C(S2), C(S2)], [C(S2), C(-S2)]],
        S: [[C(1), C(0)], [C(0), C(0, 1)]],
        SDG: [[C(1), C(0)], [C(0), C(0, -1)]],
        T: [[C(1), C(0)], [C(0), C(S2, S2)]],
        TDG: [[C(1), C(0)], [C(0), C(S2, -S2)]],
        SX: [[C(0.5, 0.5), C(0.5, -0.5)], [C(0.5, -0.5), C(0.5, 0.5)]]
    };

    function Rx(t) { var c = Math.cos(t / 2), s = Math.sin(t / 2); return [[C(c), C(0, -s)], [C(0, -s), C(c)]]; }
    function Ry(t) { var c = Math.cos(t / 2), s = Math.sin(t / 2); return [[C(c), C(-s)], [C(s), C(c)]]; }
    function Rz(t) { return [[cexp(-t / 2), C(0)], [C(0), cexp(t / 2)]]; }
    function P(p) { return [[C(1), C(0)], [C(0), cexp(p)]]; }
    function U3(th, ph, lam) {
        var ct = Math.cos(th / 2), st = Math.sin(th / 2);
        return [
            [C(ct), cscl(cexp(lam), -st)],
            [cmul(cexp(ph), C(st)), cmul(cexp(ph + lam), C(ct))]
        ];
    }

    var PAULI = { X: GATES.X, Y: GATES.Y, Z: GATES.Z };

    /* Determinant of a 2x2 complex matrix */
    function det2(U) {
        return csub(cmul(U[0][0], U[1][1]), cmul(U[0][1], U[1][0]));
    }

    /* Principal matrix power U^t : continuous path with U^0 = I, U^1 = U.
       Write U = sqrt(det) * V with V in SU(2); V = a*I - i*(b.sigma). */
    function gatePow(U, t) {
        var d = det2(U);
        var da = carg(d);
        var scale = cexp(t * da / 2);               // (sqrt det)^t
        var inv = cexp(-da / 2);                    // 1 / sqrt(det)
        var V = [[cmul(U[0][0], inv), cmul(U[0][1], inv)],
                 [cmul(U[1][0], inv), cmul(U[1][1], inv)]];

        var a = V[0][0].re;
        var bx = -V[0][1].im;
        var by = -V[0][1].re;
        var bz = -V[0][0].im;
        var nb = Math.sqrt(bx * bx + by * by + bz * bz);
        if (nb < 1e-12) {
            return [[scale, C(0)], [C(0), scale]];
        }
        var half = Math.atan2(nb, a) * t;           // t * (theta/2)
        var ca = Math.cos(half), sa = Math.sin(half);
        var nx = bx / nb, ny = by / nb, nz = bz / nb;
        var M = [
            [C(ca, -sa * nz), C(-sa * ny, -sa * nx)],
            [C(sa * ny, -sa * nx), C(ca, sa * nz)]
        ];
        return [[cmul(scale, M[0][0]), cmul(scale, M[0][1])],
                [cmul(scale, M[1][0]), cmul(scale, M[1][1])]];
    }

    /* Axis + angle of the Bloch rotation induced by a 2x2 unitary. */
    function gateAxisAngle(U) {
        var d = det2(U);
        var inv = cexp(-carg(d) / 2);
        var V = [[cmul(U[0][0], inv), cmul(U[0][1], inv)],
                 [cmul(U[1][0], inv), cmul(U[1][1], inv)]];
        var a = V[0][0].re;
        var bx = -V[0][1].im, by = -V[0][1].re, bz = -V[0][0].im;
        var nb = Math.sqrt(bx * bx + by * by + bz * bz);
        if (nb < 1e-12) return { axis: [0, 0, 1], angle: 0 };
        return { axis: [bx / nb, by / nb, bz / nb], angle: 2 * Math.atan2(nb, a) };
    }

    /* Rodrigues rotation of a 3-vector about a unit axis */
    function rotate3(v, axis, ang) {
        var n = axis, c = Math.cos(ang), s = Math.sin(ang);
        var dot = n[0] * v[0] + n[1] * v[1] + n[2] * v[2];
        var cr = [n[1] * v[2] - n[2] * v[1],
                  n[2] * v[0] - n[0] * v[2],
                  n[0] * v[1] - n[1] * v[0]];
        return [
            v[0] * c + cr[0] * s + n[0] * dot * (1 - c),
            v[1] * c + cr[1] * s + n[1] * dot * (1 - c),
            v[2] * c + cr[2] * s + n[2] * dot * (1 - c)
        ];
    }

    /* ------------------------------------------------------------------ *
     * 3. Statevector engine                                              *
     * ------------------------------------------------------------------ */
    function zeroState(n) {
        var len = 1 << n, s = new Array(len);
        for (var i = 0; i < len; i++) s[i] = C(i === 0 ? 1 : 0);
        return s;
    }

    function fromAmplitudes(list) {
        return list.map(function (a) { return C(a[0], a[1]); });
    }

    /* Bit position of qubit q inside the integer basis index */
    function bitOf(q, n) { return 1 << (n - 1 - q); }

    function apply1q(state, U, q, n) {
        var bit = bitOf(q, n);
        var out = state.slice();
        for (var i = 0; i < state.length; i++) {
            if (i & bit) continue;
            var j = i | bit;
            var a = state[i], b = state[j];
            out[i] = cadd(cmul(U[0][0], a), cmul(U[0][1], b));
            out[j] = cadd(cmul(U[1][0], a), cmul(U[1][1], b));
        }
        return out;
    }

    /* Controlled-U with control c, target t */
    function applyCtrl(state, U, c, t, n) {
        if (c === t) return state.slice();
        var bc = bitOf(c, n), bt = bitOf(t, n);
        var out = state.slice();
        for (var i = 0; i < state.length; i++) {
            if (i & bt) continue;
            var j = i | bt;
            if (i & bc) {
                var a = state[i], b = state[j];
                out[i] = cadd(cmul(U[0][0], a), cmul(U[0][1], b));
                out[j] = cadd(cmul(U[1][0], a), cmul(U[1][1], b));
            } else {
                out[i] = state[i]; out[j] = state[j];
            }
        }
        return out;
    }

    /* General 4x4 two-qubit operator on qubits a and b.
       Row/column index = 2*(value of a) + (value of b). */
    var SWAP4 = [
        [C(1), C(0), C(0), C(0)],
        [C(0), C(0), C(1), C(0)],
        [C(0), C(1), C(0), C(0)],
        [C(0), C(0), C(0), C(1)]
    ];

    function apply2q(state, M, a, b, n) {
        if (a === b) return state.slice();
        var ba = bitOf(a, n), bb = bitOf(b, n);
        var out = new Array(state.length);
        for (var k = 0; k < state.length; k++) out[k] = C(0, 0);
        for (var i = 0; i < state.length; i++) {
            if (i & ba) continue;
            if (i & bb) continue;
            var idx = [i, i | bb, i | ba, i | ba | bb];
            for (var r = 0; r < 4; r++) {
                var acc = C(0, 0);
                for (var c2 = 0; c2 < 4; c2++) {
                    var m = M[r][c2];
                    if (m.re === 0 && m.im === 0) continue;
                    acc = cadd(acc, cmul(m, state[idx[c2]]));
                }
                out[idx[r]] = acc;
            }
        }
        return out;
    }

    function cnot(state, c, t, n) { return applyCtrl(state, GATES.X, c, t, n); }
    function cy(state, c, t, n) { return applyCtrl(state, GATES.Y, c, t, n); }
    function cz(state, c, t, n) { return applyCtrl(state, GATES.Z, c, t, n); }
    function ch(state, c, t, n) { return applyCtrl(state, GATES.H, c, t, n); }
    function cphase(state, c, t, n, phi) { return applyCtrl(state, P(phi), c, t, n); }
    function swap(state, a, b, n) { return apply2q(state, SWAP4, a, b, n); }

    function probs(state) {
        return state.map(function (a) { return a.re * a.re + a.im * a.im; });
    }

    /* Remove the physically irrelevant global phase: make the first
       non-negligible amplitude real and positive. */
    function canonical(state) {
        var pivot = -1;
        for (var i = 0; i < state.length; i++) {
            if (cabs(state[i]) > 1e-9) { pivot = i; break; }
        }
        if (pivot < 0) return state.slice();
        var ph = carg(state[pivot]);
        var f = cexp(-ph);
        return state.map(function (a) { return cmul(a, f); });
    }

    function norm(state) {
        var s = 0;
        for (var i = 0; i < state.length; i++) s += state[i].re * state[i].re + state[i].im * state[i].im;
        return Math.sqrt(s);
    }

    function sample(p) {
        var r = Math.random(), acc = 0;
        for (var i = 0; i < p.length; i++) { acc += p[i]; if (r < acc) return i; }
        return p.length - 1;
    }

    function sampleMany(p, shots) {
        var counts = new Array(p.length).fill(0);
        for (var s = 0; s < shots; s++) counts[sample(p)]++;
        return counts;
    }

    /* Collapse: measure qubit q, return {outcome, state} */
    function measureQubit(state, q, n) {
        var bit = bitOf(q, n);
        var p1 = 0;
        for (var i = 0; i < state.length; i++) {
            if (i & bit) p1 += state[i].re * state[i].re + state[i].im * state[i].im;
        }
        var outcome = Math.random() < p1 ? 1 : 0;
        var f = outcome ? 1 / Math.sqrt(p1 || 1e-300) : 1 / Math.sqrt(Math.max(1 - p1, 1e-300));
        var out = state.map(function (a, i) {
            var keep = ((i & bit) ? 1 : 0) === outcome;
            return keep ? cscl(a, f) : C(0, 0);
        });
        return { outcome: outcome, p1: p1, state: out };
    }

    /* Reduced Bloch vector of qubit q */
    function bloch(state, q, n) {
        var bit = bitOf(q, n);
        var x = 0, y = 0, z = 0;
        for (var i = 0; i < state.length; i++) {
            if (i & bit) continue;
            var j = i | bit;
            var al = state[i], be = state[j];
            var u = cmul(cconj(al), be);       // alpha* beta
            x += 2 * u.re;
            y += 2 * u.im;
            z += (al.re * al.re + al.im * al.im) - (be.re * be.re + be.im * be.im);
        }
        return { x: x, y: y, z: z, r: Math.sqrt(x * x + y * y + z * z) };
    }

    /* <psi| O_q |psi> for O in {X,Y,Z} */
    function expect(state, q, n, which) {
        return bloch(state, q, n)[which.toLowerCase()];
    }

    /* Two-qubit entanglement measures for a pure state */
    function entanglement(state) {
        if (state.length !== 4) {
            return { concurrence: 0, entropy: 0, lambda: [1, 0] };
        }
        var a = state[0], b = state[1], c = state[2], d = state[3];
        var det = csub(cmul(a, d), cmul(b, c));
        var conc = 2 * cabs(det);
        if (conc < 0) conc = 0;
        if (conc > 1) conc = 1;
        var s = Math.sqrt(Math.max(0, 1 - conc * conc));
        var lp = (1 + s) / 2, lm = (1 - s) / 2;
        function h(p) { return p <= 0 || p >= 1 ? 0 : -p * Math.log2(p); }
        var ent = h(lp) + h(lm);
        return { concurrence: conc, entropy: ent, lambda: [lp, lm] };
    }

    /* Correlation <psi| A (x) B |psi> for Pauli strings on a 2-qubit state */
    function corr2(state, pa, pb) {
        // Build the 4x4 operator A (x) B and evaluate <psi|O|psi>
        var A = PAULI[pa], B = PAULI[pb];
        var total = C(0, 0);
        for (var i = 0; i < 4; i++) {
            var ia = (i >> 1) & 1, ib = i & 1;
            for (var j = 0; j < 4; j++) {
                var ja = (j >> 1) & 1, jb = j & 1;
                var m = cmul(A[ia][ja], B[ib][jb]);
                if (m.re === 0 && m.im === 0) continue;
                total = cadd(total, cmul(cmul(cconj(state[i]), m), state[j]));
            }
        }
        return total.re;
    }

    /* ------------------------------------------------------------------ *
     * 4. Formatting helpers                                              *
     * ------------------------------------------------------------------ */
    function labels(n) {
        var out = [];
        for (var i = 0; i < (1 << n); i++) {
            var s = i.toString(2);
            while (s.length < n) s = '0' + s;
            out.push(s);
        }
        return out;
    }

    function num(v, dp) {
        dp = dp === undefined ? 3 : dp;
        if (Object.is(v, -0)) v = 0;
        var s = v.toFixed(dp);
        if (s === '-' + (0).toFixed(dp)) s = (0).toFixed(dp);
        return s;
    }

    /* "a + bi" */
    function fmt(a, dp) {
        dp = dp === undefined ? 3 : dp;
        a = snap(a, 1e-9);
        var re = a.re, im = a.im;
        if (Math.abs(im) < 1e-9) return num(re, dp);
        var sign = im >= 0 ? '+' : '−';
        return num(re, dp) + ' ' + sign + ' ' + num(Math.abs(im), dp) + 'i';
    }

    /* "r e^{i th}" with th in degrees */
    function fmtPolar(a, dp) {
        dp = dp === undefined ? 3 : dp;
        var r = cabs(a), th = carg(a) * 180 / Math.PI;
        if (r < 1e-9) return '0';
        if (Math.abs(th) < 0.5) return num(r, dp);
        return num(r, dp) + ' e^{' + num(th, 1) + '°i}';
    }

    function polar(a) { return { r: cabs(a), th: carg(a) }; }
    function deg(rad) { return rad * 180 / Math.PI; }

    /* pretty ket: sum of amplitude * |bits> */
    function ketString(state, n, dp) {
        dp = dp === undefined ? 3 : dp;
        var labs = labels(n), parts = [];
        for (var i = 0; i < state.length; i++) {
            var a = snap(state[i], 1e-9);
            if (cabs(a) < 1e-9) continue;
            parts.push(fmt(a, dp) + '|' + labs[i] + '⟩');
        }
        return parts.length ? parts.join(' + ') : '0';
    }

    /* ------------------------------------------------------------------ *
     * 5. Bloch sphere renderer                                           *
     * ------------------------------------------------------------------ */
    function Bloch(canvas, opts) {
        opts = opts || {};
        this.canvas = canvas;
        this.ctx = canvas.getContext('2d');
        this.az = opts.az === undefined ? -0.95 : opts.az;
        this.el = opts.el === undefined ? 0.30 : opts.el;
        this.main = { x: 0, y: 0, z: 1, color: opts.color || '#000f91' };
        this.extra = [];                 // [{x,y,z,color,label,dashed}]
        this.trail = [];
        this.maxTrail = opts.maxTrail === undefined ? 90 : opts.maxTrail;
        this.showLabels = opts.labels !== false;
        this.showGrid = opts.grid !== false;
        this.showDrop = opts.drop !== false;
        this.showSphere = opts.sphere !== false;
        this.spin = false;
        this.onchange = null;
        this._drag = false;
        this._px = 0; this._py = 0;
        this._w = 0; this._h = 0;
        this._raf = null;
        this._bind();
        this.resize();
        var self = this;
        if (typeof ResizeObserver !== 'undefined') {
            try {
                this._ro = new ResizeObserver(function () { self.resize(); });
                this._ro.observe(canvas);
            } catch (e) { /* ignore */ }
        }
    }

    Bloch.prototype._bind = function () {
        var self = this, cv = this.canvas;
        cv.style.touchAction = 'none';
        cv.style.cursor = 'grab';

        function down(e) {
            self._drag = true;
            self.spin = false;
            var p = pt(e);
            self._px = p.x; self._py = p.y;
            cv.style.cursor = 'grabbing';
            e.preventDefault();
        }
        function move(e) {
            if (!self._drag) return;
            var p = pt(e);
            var dx = p.x - self._px, dy = p.y - self._py;
            self._px = p.x; self._py = p.y;
            self.az += dx * 0.010;
            self.el += dy * 0.008;
            if (self.el > 1.45) self.el = 1.45;
            if (self.el < -1.45) self.el = -1.45;
            self.draw();
            if (self.onchange) self.onchange();
            e.preventDefault();
        }
        function up() {
            self._drag = false;
            cv.style.cursor = 'grab';
        }
        function pt(e) {
            if (e.touches && e.touches.length) return { x: e.touches[0].clientX, y: e.touches[0].clientY };
            return { x: e.clientX, y: e.clientY };
        }
        cv.addEventListener('mousedown', down);
        window.addEventListener('mousemove', move);
        window.addEventListener('mouseup', up);
        cv.addEventListener('touchstart', down, { passive: false });
        cv.addEventListener('touchmove', move, { passive: false });
        window.addEventListener('touchend', up);
        cv.addEventListener('dblclick', function () {
            self.az = -0.95; self.el = 0.30; self.draw();
        });
    };

    Bloch.prototype.resize = function () {
        var cv = this.canvas;
        var w = cv.clientWidth || 360, h = cv.clientHeight || 360;
        var dpr = window.devicePixelRatio || 1;
        cv.width = Math.round(w * dpr);
        cv.height = Math.round(h * dpr);
        this.ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
        this._w = w; this._h = h;
        this.draw();
    };

    Bloch.prototype.proj = function (x, y, z) {
        var ca = Math.cos(this.az), sa = Math.sin(this.az);
        var ce = Math.cos(this.el), se = Math.sin(this.el);
        var x1 = x * ca - y * sa;
        var y1 = x * sa + y * ca;
        return { sx: x1, sy: z * ce - y1 * se, d: y1 * ce + z * se };
    };

    Bloch.prototype.set = function (x, y, z) {
        if (typeof x === 'object') { this.main.z = x.z; this.main.y = x.y; this.main.x = x.x; }
        else { this.main.x = x; this.main.y = y; this.main.z = z; }
        this.draw();
    };

    Bloch.prototype.setExtras = function (list) { this.extra = list || []; this.draw(); };
    Bloch.prototype.pushTrail = function (v) {
        this.trail.push(v || { x: this.main.x, y: this.main.y, z: this.main.z });
        if (this.trail.length > this.maxTrail) this.trail.shift();
    };
    Bloch.prototype.clearTrail = function () { this.trail = []; };
    Bloch.prototype.setSpin = function (on) {
        var self = this;
        this.spin = !!on;
        if (this._raf) { cancelAnimationFrame(this._raf); this._raf = null; }
        if (this.spin) {
            (function loop() {
                if (!self.spin) return;
                self.az += 0.005;
                self.draw();
                self._raf = requestAnimationFrame(loop);
            })();
        }
    };

    Bloch.prototype.draw = function () {
        var ctx = this.ctx, w = this._w, h = this._h;
        if (!ctx || w === 0 || h === 0) return;
        ctx.clearRect(0, 0, w, h);

        var cx = w / 2, cy = h / 2;
        var R = Math.min(w, h) * 0.36;
        var self = this;
        function P(p) { return { X: cx + p.sx * R, Y: cy - p.sy * R, d: p.d }; }

        /* --- body of the sphere --- */
        if (this.showSphere) {
            var g = ctx.createRadialGradient(cx - R * 0.35, cy - R * 0.4, R * 0.1, cx, cy, R * 1.15);
            g.addColorStop(0, 'rgba(255,255,255,0.98)');
            g.addColorStop(0.55, 'rgba(240,244,252,0.92)');
            g.addColorStop(1, 'rgba(214,224,244,0.92)');
            ctx.beginPath();
            ctx.arc(cx, cy, R, 0, Math.PI * 2);
            ctx.fillStyle = g;
            ctx.fill();
            ctx.lineWidth = 1;
            ctx.strokeStyle = 'rgba(0,15,145,0.22)';
            ctx.stroke();
        }

        /* --- wireframe, depth sorted --- */
        if (this.showGrid) {
            var segs = [];
            var NSEG = 40, i, k, m;
            var NLAT = 6;
            for (k = 1; k < NLAT; k++) {
                var th = Math.PI * k / NLAT;
                var zz = Math.cos(th), rr = Math.sin(th);
                for (i = 0; i < NSEG; i++) {
                    var a0 = 2 * Math.PI * i / NSEG, a1 = 2 * Math.PI * (i + 1) / NSEG;
                    segs.push({
                        p0: this.proj(rr * Math.cos(a0), rr * Math.sin(a0), zz),
                        p1: this.proj(rr * Math.cos(a1), rr * Math.sin(a1), zz),
                        eq: Math.abs(zz) < 1e-9
                    });
                }
            }
            for (m = 0; m < 6; m++) {
                var phi = Math.PI * m / 6;
                for (i = 0; i < 32; i++) {
                    var t0 = Math.PI * i / 32, t1 = Math.PI * (i + 1) / 32;
                    segs.push({
                        p0: this.proj(Math.sin(t0) * Math.cos(phi), Math.sin(t0) * Math.sin(phi), Math.cos(t0)),
                        p1: this.proj(Math.sin(t1) * Math.cos(phi), Math.sin(t1) * Math.sin(phi), Math.cos(t1)),
                        eq: false
                    });
                }
            }
            segs.sort(function (a, b) { return (a.p0.d + a.p1.d) - (b.p0.d + b.p1.d); });
            for (i = 0; i < segs.length; i++) {
                var s = segs[i];
                var dd = (s.p0.d + s.p1.d) / 2;
                var t = (dd + 1) / 2;
                var A0 = P(s.p0), A1 = P(s.p1);
                ctx.beginPath();
                ctx.moveTo(A0.X, A0.Y);
                ctx.lineTo(A1.X, A1.Y);
                ctx.strokeStyle = 'rgba(0,15,145,' + (0.05 + 0.28 * t * t).toFixed(3) + ')';
                ctx.lineWidth = s.eq ? 1.2 : 0.8;
                ctx.stroke();
            }
        }

        /* --- axes --- */
        var axes = [
            { v: [1, 0, 0], c: '#c2410c', lab: ['|+⟩', '|−⟩'] },
            { v: [0, 1, 0], c: '#047857', lab: ['|+i⟩', '|−i⟩'] },
            { v: [0, 0, 1], c: '#000f91', lab: ['|0⟩', '|1⟩'] }
        ];
        for (var ai = 0; ai < axes.length; ai++) {
            var ax = axes[ai];
            var tip = this.proj(ax.v[0], ax.v[1], ax.v[2]);
            var tail = this.proj(-ax.v[0], -ax.v[1], -ax.v[2]);
            var A = P(tail), B = P(tip);
            ctx.beginPath();
            ctx.moveTo(A.X, A.Y);
            ctx.lineTo(B.X, B.Y);
            ctx.strokeStyle = ax.c;
            ctx.globalAlpha = 0.35 + 0.4 * ((tip.d + 1) / 2);
            ctx.lineWidth = 1.3;
            ctx.setLineDash([5, 4]);
            ctx.stroke();
            ctx.setLineDash([]);
            ctx.globalAlpha = 1;

            if (this.showLabels) {
                ctx.font = '600 12px "JetBrains Mono", "Menlo", monospace';
                ctx.fillStyle = ax.c;
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                var off = 14;
                var dir = B.Y > cy ? 1 : -1;
                ctx.fillText(ax.lab[0], B.X + (B.X - cx > 0 ? off : -off) * 0.6, B.Y + dir * 12);
                ctx.globalAlpha = 0.65;
                ctx.fillText(ax.lab[1], A.X + (A.X - cx > 0 ? off : -off) * 0.6, A.Y - dir * 12);
                ctx.globalAlpha = 1;
            }
        }

        /* --- trail --- */
        if (this.trail.length > 1) {
            for (var ti = 1; ti < this.trail.length; ti++) {
                var q0 = this.trail[ti - 1], q1 = this.trail[ti];
                var B0 = P(this.proj(q0.x, q0.y, q0.z));
                var B1 = P(this.proj(q1.x, q1.y, q1.z));
                ctx.beginPath();
                ctx.moveTo(B0.X, B0.Y);
                ctx.lineTo(B1.X, B1.Y);
                ctx.strokeStyle = 'rgba(128,90,213,' + (0.05 + 0.30 * (ti / this.trail.length)).toFixed(3) + ')';
                ctx.lineWidth = 2;
                ctx.stroke();
            }
        }

        /* --- drop lines / projections --- */
        function drawVector(v, color, width, dashed, label) {
            var r = Math.sqrt(v.x * v.x + v.y * v.y + v.z * v.z);
            if (r < 1e-9) return;
            var tipP = P(self.proj(v.x, v.y, v.z));
            var org = P(self.proj(0, 0, 0));

            if (self.showDrop && r > 0.06) {
                var flat = P(self.proj(v.x, v.y, 0));
                ctx.beginPath();
                ctx.setLineDash([3, 3]);
                ctx.strokeStyle = 'rgba(95,99,104,0.45)';
                ctx.lineWidth = 1;
                ctx.moveTo(org.X, org.Y); ctx.lineTo(flat.X, flat.Y);
                ctx.lineTo(tipP.X, tipP.Y);
                ctx.stroke();
                ctx.setLineDash([]);
            }

            ctx.beginPath();
            ctx.moveTo(org.X, org.Y);
            ctx.lineTo(tipP.X, tipP.Y);
            ctx.strokeStyle = color;
            ctx.lineWidth = width;
            ctx.lineCap = 'round';
            if (dashed) ctx.setLineDash([6, 4]);
            ctx.stroke();
            ctx.setLineDash([]);

            /* arrow head */
            var dx = tipP.X - org.X, dy = tipP.Y - org.Y;
            var L = Math.hypot(dx, dy) || 1;
            var ux = dx / L, uy = dy / L;
            var hs = 9;
            ctx.beginPath();
            ctx.moveTo(tipP.X, tipP.Y);
            ctx.lineTo(tipP.X - ux * hs - uy * hs * 0.45, tipP.Y - uy * hs + ux * hs * 0.45);
            ctx.lineTo(tipP.X - ux * hs + uy * hs * 0.45, tipP.Y - uy * hs - ux * hs * 0.45);
            ctx.closePath();
            ctx.fillStyle = color;
            ctx.fill();

            ctx.beginPath();
            ctx.arc(org.X, org.Y, 3.2, 0, Math.PI * 2);
            ctx.fillStyle = '#202124';
            ctx.fill();

            if (label) {
                ctx.font = '600 11px "JetBrains Mono", monospace';
                ctx.fillStyle = color;
                ctx.textAlign = 'left';
                ctx.textBaseline = 'middle';
                ctx.fillText(label, tipP.X + 8, tipP.Y - 8);
            }
        }

        var ei;
        for (ei = 0; ei < this.extra.length; ei++) {
            var ev = this.extra[ei];
            drawVector(ev, ev.color || '#805ad5', ev.width || 2.4, !!ev.dashed, ev.label);
        }
        drawVector(this.main, this.main.color, 3.4, false, this.main.label);

        /* --- corner hint --- */
        ctx.font = '10px "Inter", sans-serif';
        ctx.fillStyle = 'rgba(95,99,104,0.75)';
        ctx.textAlign = 'left';
        ctx.textBaseline = 'bottom';
        ctx.fillText('drag to rotate · double-click to reset', 8, h - 6);
    };

    /* ------------------------------------------------------------------ *
     * 6. Misc DOM helpers                                                *
     * ------------------------------------------------------------------ */
    function el(id) { return document.getElementById(id); }
    function clamp(v, a, b) { return v < a ? a : (v > b ? b : v); }

    /* Shared light-theme palette for Chart.js figures */
    var CHART_FONT = { family: '"JetBrains Mono", "Menlo", monospace', size: 11 };
    var CHART_INK = '#5f6368';
    var CHART_GRID = 'rgba(15,23,42,0.07)';

    function barChart(canvasEl, labelsArr, dataArr, opts) {
        opts = opts || {};
        if (!global.Chart) return null;
        if (canvasEl.__chart) canvasEl.__chart.destroy();
        var ds = [{
            label: opts.label || 'Probability',
            data: dataArr,
            backgroundColor: opts.colors || 'rgba(0,15,145,0.75)',
            borderRadius: 5,
            borderSkipped: false,
            barPercentage: 0.82,
            categoryPercentage: 0.85
        }];
        if (opts.data2) {
            ds.push({
                label: opts.label2 || 'Reference',
                data: opts.data2,
                backgroundColor: opts.colors2 || 'rgba(180,83,9,0.55)',
                borderRadius: 5,
                borderSkipped: false,
                barPercentage: 0.82,
                categoryPercentage: 0.85
            });
        }
        canvasEl.__chart = new global.Chart(canvasEl.getContext('2d'), {
            type: 'bar',
            data: { labels: labelsArr, datasets: ds },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                animation: { duration: opts.animate === false ? 0 : 320 },
                plugins: {
                    legend: {
                        display: !!opts.data2,
                        labels: { color: CHART_INK, font: CHART_FONT, boxWidth: 11, usePointStyle: true }
                    },
                    tooltip: {
                        backgroundColor: '#202124',
                        titleFont: CHART_FONT, bodyFont: CHART_FONT,
                        callbacks: {
                            label: function (c) {
                                return (opts.unit === 'count' ? '' : '') + c.parsed.y.toFixed(4);
                            }
                        }
                    }
                },
                scales: {
                    x: { grid: { display: false }, ticks: { color: CHART_INK, font: CHART_FONT } },
                    y: {
                        beginAtZero: true,
                        max: opts.max,
                        grid: { color: CHART_GRID },
                        ticks: { color: CHART_INK, font: CHART_FONT }
                    }
                }
            }
        });
        return canvasEl.__chart;
    }

    /* ------------------------------------------------------------------ *
     * 7. Export                                                          *
     * ------------------------------------------------------------------ */
    var QC = {
        C: C, cadd: cadd, csub: csub, cmul: cmul, cscl: cscl, cconj: cconj,
        cabs: cabs, carg: carg, cexp: cexp, cdiv: cdiv, snap: snap,
        GATES: GATES, PAULI: PAULI, SWAP4: SWAP4,
        Rx: Rx, Ry: Ry, Rz: Rz, P: P, U3: U3,
        zeroState: zeroState, fromAmplitudes: fromAmplitudes, bitOf: bitOf,
        apply1q: apply1q, applyCtrl: applyCtrl, apply2q: apply2q,
        cnot: cnot, cy: cy, cz: cz, ch: ch, cphase: cphase, swap: swap,
        probs: probs, norm: norm, canonical: canonical, sample: sample, sampleMany: sampleMany,
        measureQubit: measureQubit, bloch: bloch, expect: expect,
        entanglement: entanglement, corr2: corr2,
        gatePow: gatePow, gateAxisAngle: gateAxisAngle, rotate3: rotate3,
        labels: labels, num: num, fmt: fmt, fmtPolar: fmtPolar, polar: polar,
        deg: deg, ketString: ketString,
        Bloch: Bloch, barChart: barChart, el: el, clamp: clamp
    };

    global.QC = QC;
    if (typeof module !== 'undefined' && module.exports) module.exports = QC;

})(typeof window !== 'undefined' ? window : globalThis);
