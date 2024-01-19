const $searchbar = $("#searchbar");
const $giflist = $("#results_list");
const url = "http://127.0.0.1:5000/";

$("#search_form").on("submit", async function (e) {
  console.log("HEEEEEY");

  e.preventDefault();
  try {
    const response = await axios.get(`/search?searchbar=${$searchbar.val()}`);
    console.log(response);
    Appendhtml(response.data);
    
  } catch (error) {
    console.log(error);
  }

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

$("#results_list").on("click", GetArtistDetails);
