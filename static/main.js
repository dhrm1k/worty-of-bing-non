async function load() {
    let url = '/api/feed';
    let obj = null;
    
    try {
        obj = await (await fetch(url)).json();
    } catch(e) {
        console.log('error');
    }
    
  name = obj.thoughts[0];

  console.log(name)
}

load();
