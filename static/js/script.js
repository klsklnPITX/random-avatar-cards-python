function searchInput(avatars) {
    var searchBoxInput = document.getElementById("searchBox").value;
    var avatars_obj = JSON.parse(avatars)
    const filteredAvatars = avatars_obj.filter(avatars_obj => {
        return (avatars_obj.name.toLowerCase().includes(searchBoxInput.toLowerCase()))
    });
    console.log(avatars);
}
