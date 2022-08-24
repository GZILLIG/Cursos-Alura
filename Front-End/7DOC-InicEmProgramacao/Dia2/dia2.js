const formulario = document.querySelector('.formulario');

function checkForm(){
    //Adquire as informações fornecidas no formulário
    let nome = document.getElementById('nome').value;
    let idade = document.getElementById('idade').value;
    let linguagemProgramacao = document.getElementById('linguagem-programacao').value;
    
    //Monta a frase de resposta
    let mensagem = `Olá ${nome}, você tem ${idade} anos e já está aprendendo ${linguagemProgramacao}!`;

    
    
    //Para de exibir o formulário
    document.getElementById("perguntas").style.display = "none";
    
    //Começa a exibir a resposta e a segunda pergunta
    document.getElementById("resposta1").style.display = "block";

    //Monta a frase da segunda pergunta
    let textopergunta2 = `Você gosta de estudar ${linguagemProgramacao}?`;

    //Exibe a frase de resposta
    document.getElementById("formResposta").innerHTML = mensagem;

    //Exibe a legenda da segunda pergunta
    document.getElementById("pergunta2").innerHTML = textopergunta2;

    return false;
  }

  function checkMenuSelect(){
    let respostaGosta = document.getElementById('gosta').value;

      if (respostaGosta == 'sim'){
        document.getElementById("resposta2").innerHTML = "Muito bom! Continue estudando e você terá muito sucesso.";
      }

      else if (respostaGosta == 'nao'){
        document.getElementById("resposta2").innerHTML = "Ahh que pena... Já tentou aprender outras linguagens?";
      }

      else{
        document.getElementById("resposta2").innerHTML = "";
      }

    
  }
  
