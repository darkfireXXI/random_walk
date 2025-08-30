// function fetchCategories() {
//     fetch('http://0.0.0.0:50051/category-group/list')
//         .then(response => response.json())
//         .then(data => {
//             const categoryList = document.getElementById('category-list');
//             data.forEach(item => {
//                 const listItem = document.createElement('li');
//                 listItem.textContent = item.name;
//                 categoryList.appendChild(listItem);
//             });
//         })
//         .catch(error => {
//             console.error('Error fetching categories:', error);
//         });
// }

// window.onload = fetchCategories;



function fetchCategories() {
    fetch('http://0.0.0.0:50051/category-group/list')
        .then(response => response.json())
        .then(data => {
            const categoryList = document.getElementById('category-list');
            categoryList.innerHTML = '';
            if (data.length === 0) {
                const noCategoriesButton = document.createElement('button');
                noCategoriesButton.textContent = 'Nothing interesting? Why don\'t you try finding something here!';
                noCategoriesButton.style.padding = '10px 20px';
                noCategoriesButton.style.backgroundColor = '#ff3333'; // Red background for emphasis
                noCategoriesButton.style.color = 'white';
                noCategoriesButton.style.border = 'none';
                noCategoriesButton.style.borderRadius = '10px';
                noCategoriesButton.style.cursor = 'pointer';
                categoryList.appendChild(noCategoriesButton);
            } else {
                data.forEach(item => {
                    const listItem = document.createElement('li');
                    listItem.textContent = item.name;
                    categoryList.appendChild(listItem);
                });
            }
        })
        .catch(error => {
            console.error('Error fetching categories:', error);
        });
}

window.onload = fetchCategories;
