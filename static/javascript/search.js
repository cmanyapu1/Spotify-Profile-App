const $searchbar = $("#searchbar");
const $giflist = $("#results_list");
const url = "http://127.0.0.1:5000/";

$("#search_form").on("submit", async function (e) {
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
  $("#results_list").empty();
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

  window.location.href = `/results/${targetartist}`;
  // const result = await axios.get(`/results/${targetartist}`);

  // console.log(result);
  // toggleclick.after(result.data);
}

$("#results_list").on("click", GetArtistDetails);

document.addEventListener('DOMContentLoaded', function () {
  // Get a reference to the search button and the selectArtist element
  var searchForm = document.querySelector('#search_form');
  var selectArtist = document.querySelector('#selectArtist');

  // Add a click event listener to the search button
  searchForm.addEventListener('submit', function (event) {
      // Prevent the default form submission behavior
      event.preventDefault();
      // Show the selectArtist element
      selectArtist.style.display = 'block';
  });
});

async function GetLyric (evt) {
  const toggleclick = $(evt.target);
  const artistSelected = document.querySelector('#selectArtist').value;
  var samplelyric = document.querySelector('#SampleLyric');
  const response = await axios.get(`/find_me_a_lyric=${artistSelected}`, );
  $('#lyrics-from-openai').html(response.data);
  samplelyric.style.display = 'none';
}
$('#OpenAILyric').on('click', GetLyric);

