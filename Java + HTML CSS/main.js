
//Encontra no HTML todas as linhas com a classe "tecla", pesentes nos botões
const listaDeTeclas = document.querySelectorAll('.tecla');

//laço para consultar toda a lista listaDeTeclas
for (let contador = 0; contador < listaDeTeclas.length; contador++) {

    //extrai o #id de cada uma das teclas
    const tecla = listaDeTeclas[contador];
    const instrumento = tecla.classList[1];
    const idAudio = `#som_${instrumento}`; //template string

    //verifica SE o botão foi clicado
    tecla.onclick = function () {
        tocaSom(idAudio);
    }

    //verifica SE as teclas de ativação Enter ou Space foram pressionadas
    tecla.onkeydown = function (evento) {
        if (evento.code == "Enter" || evento.code == "Space"){
        tecla.classList.add('ativa'); //deixa a tecla vermelha
        tocaSom(idAudio);      
        }
    }

    //volta para o estilo normal quando a tecla não está mais pressionada
    tecla.onkeyup = function () {
    tecla.classList.remove('ativa'); //tecla volta ao normal
    }

    //volta para o estilo normal quando o foco saiu do botão
    tecla.onblur = function (evento) {
        tecla.classList.remove('ativa');
        }
    }

//procura a linha que contem o IdAudio e grava essa linha em 'elemento'
function tocaSom (seletorAudio) {
    const elemento = document.querySelector(seletorAudio);

    //verifica SE o argumento enviado para a função 'tocaSom' é válido
    if (elemento != null && elemento.localName === 'audio'){

        elemento.play(); //toca o som
    }
    else{
        console.log("Elemento não encontrado ou seletor invalido");
    }
}
