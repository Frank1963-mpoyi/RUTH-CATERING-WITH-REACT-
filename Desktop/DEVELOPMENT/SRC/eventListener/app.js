
// get the button
var btn = document.querySelector('#btn');

// I got the button in the variable btn I want to add event to my button and perform some thing after adding event
btn.addEventListener('click' , addText);

function addText() {
    // test the operation
    //console.log('display Mpoyi is clicking ')
    
    //now the time to display in the browser
    const display =  document.querySelector('.show')
    display.innerHTML = '<h1 class="text-center"> Mpoyi Tshibuyi </h1>'
    


}


