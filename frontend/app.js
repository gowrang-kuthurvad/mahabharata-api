async function searchChar(){
let name=document.getElementById("search").value;
let res=await fetch(`http://127.0.0.1:5000/search?name=${name}`);
let data=await res.json();
let out="";
data.forEach(c=>{
out+=`<div><h3>${c.name}</h3><p>${c.description}</p></div>`;
});
document.getElementById("result").innerHTML=out;
}