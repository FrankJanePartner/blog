function toggleDropdown(elementId) {
    var dropdownContent = document.getElementById(elementId);

    if (dropdownContent.style.display === 'none') {
        dropdownContent.style.display = 'flex'; // Change display to 'flex' to show the dropdown
    } else {
        dropdownContent.style.display = 'none';
    }
}
