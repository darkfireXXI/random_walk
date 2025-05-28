// // Get the dropdown button and menu
// const dropdownButton = document.querySelector('.user-btn');
// const dropdownMenu = document.querySelector('.dropdown-menu');

// // Toggle the dropdown menu when the button is clicked
// dropdownButton.addEventListener('click', (event) => {
//   event.stopPropagation(); // Prevent click from propagating to the document
//   dropdownMenu.style.display = (dropdownMenu.style.display === 'block') ? 'none' : 'block';
// });

// // Close the dropdown menu if clicking outside the dropdown
// window.addEventListener('click', (event) => {
//   if (!event.target.closest('.dropdown')) {
//     dropdownMenu.style.display = 'none';
//   }
// });


// Get the dropdown button and menu
const dropdownButton = document.querySelector('.user-btn');
const dropdownMenu = document.querySelector('.dropdown-menu');

// Toggle the dropdown menu when the button is clicked
dropdownButton.addEventListener('click', function(event) {
  // event.stopPropagation(); // Prevent click from propagating to the document
  // Toggle the visibility of the dropdown menu
  if (dropdownMenu.style.display === 'block') {
    dropdownMenu.style.display = 'none';
  } else {
    dropdownMenu.style.display = 'block';
  }
});

// Close the dropdown menu if clicking outside
window.addEventListener('click', function(event) {
  if (!event.target.closest('.dropdown')) {
    dropdownMenu.style.display = 'none';
  }
});
