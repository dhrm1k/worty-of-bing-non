async function load() {
    let url = '/api/feed';
    let obj = null;
    
    try {
        obj = await (await fetch(url)).json();
    } catch(e) {
        console.log('error');
    }
  a = obj.thoughts.length;
  //document.getElementById("post1").innerHTML =  a; //obj.thoughts[0];

  let text = "";

  for (let i = 0; i < a; i++) {
  text += "<article><h3>" + obj.thoughts[i] + "</h3></article>";
}

  document.getElementById("posts").innerHTML = text;


  }


load();

