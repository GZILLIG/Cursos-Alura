
let numeroSecreto = getRandomIntInclusive(1,10);
let totalTentativas = 3;
let numeroTentativa = 1;

function getRandomIntInclusive(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min;
}


function checkForm(){
  if (numeroTentativa <= totalTentativas){
    //Adquire as informações fornecidas no formulário
    let chute = document.getElementById('chute').value;
    let mensagemResultado = "";

      if (chute == numeroSecreto){
        mensagemResultado = 'PARABÉNS, VOCÊ ACERTOU!';
        document.getElementById("botaoRefresh").style.display = "block";
      }
      else if (chute > numeroSecreto){
        mensagemResultado = 'Você errou, o número secreto é MENOR.';
        }
      else{
        mensagemResultado = 'Você errou, o número secreto é MAIOR.';
        }

      let mensagemConfirmacao = `Você chutou o número ${chute}. <br> ${mensagemResultado} <br><br> Tentativa ${numeroTentativa} de ${totalTentativas}.`;
      
    numeroTentativa++;
      //Exibe a frase de resposta
    document.getElementById("chute").value = "";
    document.getElementById("mensagem").innerHTML = mensagemConfirmacao ;


    
  }
  else{
    document.getElementById("mensagem").innerHTML = "Suas tentativas acabaram! Quer recomeçar?";
    document.getElementById("botaoRefresh").style.display = "block";
  }
  
  return false;
}