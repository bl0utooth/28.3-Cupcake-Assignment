const web_url = "http://localhost:5000/api";

function createCupcake(cupcake) {
    return `
      <div data-cupcake-id=${cupcake.id}>
        <li>
          ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
          <button class="delete-button">X</button>
        </li>
        <img class="Cupcake-img"
              src="${cupcake.image}"
              alt="(no image provided)">
      </div>
    `;
}

async function showCupcakeList() {
    const response = await axios.get(`${web_url}/cupcakes`);
  
    for (let cupcakeData of response.data.cupcakes) {
      let newCupcake = $(generateCupcakeHTML(cupcakeData));
      $("#cupcakes-list").append(newCupcake);
    }
}
  

$("#make_new_cupcake").on("submit", async function (evt) {
    evt.preventDefault();
  
    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();
  
    const newCupcakeResponse = await axios.post(`${web_url}/cupcakes`, {
      flavor,
      rating,
      size,
      image
    });
  
    let newCupcake = $(createCupcake(newCupcakeResponse.data.cupcake));
    $("#cupcakes-list").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");
  });
  
  
  $("#cupcakes-list").on("click", ".delete-button", async function (evt) {
    evt.preventDefault();
    let $cupcake = $(evt.target).closest("div");
    let cupcakeId = $cupcake.attr("data-cupcake-id");
  
    await axios.delete(`${web_url}/cupcakes/${cupcakeId}`);
    $cupcake.remove();
  });
  
  $(showCupcakeList);