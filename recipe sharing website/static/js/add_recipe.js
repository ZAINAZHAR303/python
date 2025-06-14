let image_container =document.querySelector("#img_container");
let image= document.querySelector("#pic_input");


image.onchange =() =>{
image_container.src= URL.createObjectURL(image.files[0]);

}
    