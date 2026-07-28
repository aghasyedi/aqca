/* js/algorithm-ui.js */
document.addEventListener('DOMContentLoaded', () => {
    // 1. Code Copy Functionality Placeholder
    const copyButtons = document.querySelectorAll('.code-header button');
    
    copyButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Find the associated code block
            const codeBlock = button.closest('.code-block').querySelector('pre');
            if (codeBlock) {
                const text = codeBlock.textContent;
                navigator.clipboard.writeText(text).then(() => {
                    const originalText = button.textContent;
                    button.textContent = 'Copied!';
                    setTimeout(() => {
                        button.textContent = originalText;
                    }, 2000);
                }).catch(err => {
                    console.error('Failed to copy text: ', err);
                });
            }
        });
    });

    // 2. Future Interactive Simulation Hooks
    // Placeholders for initialization logic of circuits, visualizers, etc.
    const simPlaceholders = document.querySelectorAll('.simulation-placeholder');
    if (simPlaceholders.length > 0) {
        console.log('Algorithm specific simulations ready for initialization.');
    }
});

function openOutputModal(btnElement) {
    // Check if modal container exists, if not, create it
    let modal = document.getElementById('global-output-modal');
    if (!modal) {
        modal = document.createElement('div');
        modal.id = 'global-output-modal';
        modal.className = 'output-modal-overlay';
        
        modal.innerHTML = `
            <div class="output-modal-content">
                <div class="output-modal-header">
                    <h3>Notebook Execution Output</h3>
                    <button class="close-modal-btn" onclick="closeOutputModal()">✕</button>
                </div>
                <div class="output-modal-body" id="global-output-modal-body">
                </div>
            </div>
        `;
        document.body.appendChild(modal);
        
        // Close on clicking outside
        modal.addEventListener('click', function(e) {
            if (e.target === modal) {
                closeOutputModal();
            }
        });
    }
    
    // Get the data payload
    const wrapper = btnElement.closest('.output-injection-wrapper');
    const dataDiv = wrapper.querySelector('.code-output-data');
    
    // Inject into modal
    const modalBody = document.getElementById('global-output-modal-body');
    modalBody.innerHTML = dataDiv.innerHTML;
    
    // Show modal
    modal.classList.add('active');
    
    // Typeset MathJax if available
    if (window.MathJax) {
        MathJax.typesetPromise([modalBody]).catch((err) => console.error(err));
    }
}

function closeOutputModal() {
    const modal = document.getElementById('global-output-modal');
    if (modal) {
        modal.classList.remove('active');
    }
}
