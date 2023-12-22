document.getElementById('verifyButton').addEventListener('click', function () {
            var inputValue = document.getElementById('Verify').value;
            var tickIcon = document.getElementById('tick');
            var loadingIcon = document.querySelector('.loading-icon');
            var errorMessage = document.querySelector('.error-message');

            // Disable the button and show loading icon
            this.disabled = true;
            loadingIcon.style.display = 'inline';
            errorMessage.style.display = 'none';

            // Simulate processing for 3 seconds (replace with your actual verification logic)
            setTimeout(function () {
                // Check if the entered value is a 12-digit number
                if (/^\d{12}$/.test(inputValue)) {
                    // Show the blue tick icon
                    tickIcon.style.display = 'inline-block';
                } else {
                    // Hide the tick icon
                    tickIcon.style.display = 'none';
                    // Show error message for invalid input
                    errorMessage.style.display = 'block';
                }

                // Re-enable the button and hide loading icon
                document.getElementById('verifyButton').disabled = false;
                loadingIcon.style.display = 'none';
            }, 3000); // 3 seconds delay
        });