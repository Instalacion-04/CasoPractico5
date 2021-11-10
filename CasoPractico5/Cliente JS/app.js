const marvel = {
  render: () => {
    // const urlApi =
    //   "https://gateway.marvel.com:443/v1/public/comics?apikey=12cc11455bd41485d596e5ba244ca4ed";
     const urlApi =
       "https://gateway.marvel.com:443/v1/public/characters?apikey=12cc11455bd41485d596e5ba244ca4ed";
    const container = document.querySelector("#contenedor-secundario");
    let contentHTML = "";
    fetch(urlApi)
      .then((res) => res.json())
      .then((json) => {
        for (const comic of json.data.results) {
          let urlComic = comic.urls[0].url;
          contentHTML += `
                <div class="contenedor-comics">
                    <a href="${urlComic}" target="_blank" class="link">
                        <img src="${comic.thumbnail.path}.${comic.thumbnail.extension}" alt="${comic.name}" class="image">
                    </a>
                    <h3 class="titulo">${comic.name}</h3>
                </div>`;
        }
        container.innerHTML = contentHTML;
      });
  },
};
marvel.render();
