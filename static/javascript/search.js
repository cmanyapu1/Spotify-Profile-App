const $searchbar = $("#searchbar");
const $giflist = $("#results_list");
const url = "http://127.0.0.1:5000/";

$("#search_form").on("submit", async function (e) {
  console.log("HEEEEEY");

  e.preventDefault();
  try {
    const response = await axios.get(`/search?q=${$searchbar}`);
  } catch (error) {
    console.log(error);
  }

  Appendhtml(response.data);
});

function Appendhtml(dataresponse) {
  for (let y = 0; y < dataresponse.length; y++) {
    $("#results_list").append(
      `<li class="artistchosen" data-artist-id=${dataresponse[y].id}> ${dataresponse[y].name} </li>
          `
    );
  }
}
async function GetArtistDetails(evt) {
  const toggleclick = $(evt.target);
  const targetartist = toggleclick.closest("li").attr("data-artist-id");

  await axios.get(`/results/${targetartist}`);
}

$(".artistchosen").on("click", ".artistchosen", GetArtistDetails);
