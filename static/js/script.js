// Handle Booking Form Submission
document.getElementById('bookingForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('/api/bookings', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('bookingResponse').innerText = data.message;
        this.reset();
    });
});

// Handle Review Form Submission
document.getElementById('reviewForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const reviewData = new FormData(this);
    fetch('/api/reviews', {
        method: 'POST',
        body: reviewData,
    })
    .then(response => response.json())
    .then(data => {
        loadReviews(); // Function to load and display reviews
        this.reset();
    });
});

// Load reviews from the server
function loadReviews() {
    fetch('/api/reviews')
        .then(response => response.json())
        .then(reviews => {
            const reviewsList = document.getElementById('reviewsList');
            reviewsList.innerHTML = ''; // Clear existing reviews
            reviews.forEach(review => {
                const div = document.createElement('div');
                div.textContent = review.text; // Assuming review has a text field
                reviewsList.appendChild(div);
            });
        });
}

// Handle Testimonial Form Submission
document.getElementById('testimonialForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const testimonialData = new FormData(this);
    fetch('/api/testimonials', {
        method: 'POST',
        body: testimonialData,
    })
    .then(response => response.json())
    .then(data => {
        alert('Testimonial submitted!');
        this.reset();
    });
});

// Handle Contact Form Submission
document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();
    const contactData = new FormData(this);
    fetch('/api/contact', {
        method: 'POST',
        body: contactData,
    })
    .then(response => response.json())
    .then(data => {
        alert('Contact request sent!');
        this.reset();
    });
});
