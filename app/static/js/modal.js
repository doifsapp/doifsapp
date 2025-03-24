var modal = document.getElementById('modal-container');
var btn = document.getElementById('create');
var close = document.getElementById('myclose');

btn.onclick = function(){
  modal.style.display = 'flex';
}

close.onclick = function(){
  modal.style.display = 'none';
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

//Adicao do item

document.querySelector('.btn-adition').addEventListener('click', function(){

    //captura o elemento selecionado
    var selectElement = document.getElementById('subject-adition');
    //captura o valor selecionado
    var selectedValue = selectElement.value;
    //verifica se um c=valor foi selecionado
    if(selectedValue){
        //cria um novo elemento span com o valor selecionado
        var newItem = document.createElement('span');
        newItem.textContent = selectedValue;

        //adicionao o novo elemento ao content

        document.getElementById('adition-content').appendChild(newItem);
        //eseta o select
        selectElement.selectedIndex = 0;
    }
});

