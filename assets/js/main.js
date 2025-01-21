function getStarted() {
    alert("Thank you for getting started! More features coming soon.");
  }


// FAQ Toggle Functionality
document.querySelectorAll('.faq-question').forEach((question) => {
    question.addEventListener('click', () => {
      const faqItem = question.parentElement;
      faqItem.classList.toggle('active');
  
      // Close other FAQ items
      document.querySelectorAll('.faq-item').forEach((item) => {
        if (item !== faqItem) {
          item.classList.remove('active');
        }
      });
    });
  });
  