async function load() {
    let url = '/api/feed';
    let obj = null;
    
    try {
        obj = await (await fetch(url)).json();
    } catch(e) {
        console.log('error');
    }
  
  document.getElementById("post1").innerHTML = obj.thoughts[0];
}

load();
