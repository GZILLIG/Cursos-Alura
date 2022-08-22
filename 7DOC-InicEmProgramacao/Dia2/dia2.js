function checkForm(){
    let nome = document.getElementById('nome').value;
    let idade = document.getElementById('idade').value;
    let linguagemProgramacao = document.getElementById('linguagem-programacao').value;

    window.alert(`Olá ${nome}, você tem ${idade} anos e já está aprendendo ${linguagemProgramacao}!` );
    
    return false;
  }

  