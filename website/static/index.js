function deleteMovie(movieId) {
  fetch("/delete-movie", {
    method: "POST",
    body: JSON.stringify({ movieId: movieId }),
  }).then((_res) => {
    window.location.href = "/mylist";
  });
}
function addMovie(movieId) {
  fetch("/mylist", {
    method: "POST",
    body: JSON.stringify({ movieId: movieId }),
  }).then((_res) => {
  });
}
