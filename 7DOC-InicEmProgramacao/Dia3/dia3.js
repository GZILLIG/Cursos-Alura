
//alert('Olá! Bem-vindo(a) ao jogo de controle de fluxos.');
//alert('Queremos conhecer mais sobre você!');


let respostaValida = false;
let resposta1;
let resposta2;
let resposta3;
let resposta4 = [];
let i=0;

// while (respostaValida == false){
//     resposta1 = prompt('Você pretende seguir para qual área? \n Digite 1 para "Front-End" \n Digite 2 para "Back-End"');
    

//     if (resposta1 == 1 ){
//         resposta1 = 'Front-end';
//         while (respostaValida == false){
//             resposta2 = prompt('Qual linguagem você prendende aprender? \n Digite 1 para "React" \n Digite 2 para "Vue"');
//             if (resposta2 == 1){
//                 respostaValida = true;
//                 resposta2 = 'React';
//             }
//             else if (resposta2 == 2){
//                 respostaValida = true;
//                 resposta2 = 'Vue';
//             }
//             else{
//                 alert('Insira uma resposta válida!');
//             }
//         }
//     }
//     else if (resposta1 == 2){
//         resposta1 = 'Back-End';
//         while (respostaValida == false){
//             resposta2 = prompt('Qual linguagem você prendende aprender? \n Digite 1 para "C#" \n Digite 2 para "Java"');
//             if (resposta2 == 1){
//                 respostaValida = true;
//                 resposta2 = 'C#';
//             }
//             else if (resposta2 == 2){
//                 respostaValida = true;
//                 resposta2 = 'Java';
//             }
//             else{
//                 alert('Insira uma resposta válida!');
//             }
//         }
//     }

//     else{
//         alert('Insira uma resposta válida!');
//     }

// }

// respostaValida = false;
// while (respostaValida == false){

//     resposta3 = prompt(`Você escolheu ser um desenvolvedor ${resposta1}, e aprender ${resposta2}! \n\n Pensa em:\n 1. Se especializar nessa área. \n 2. Seguir se desenvolvendo para ser um desenvolvedor Fullstack`);
//     if (resposta3 == 1){
//         respostaValida = true;
//         resposta3 = 'se especializar nessa linguagem.'
//     }
//     else if (resposta3 == 2){
//         respostaValida = true;
//         resposta3 = 'tornar-se um desenvolvedor Fullstack.'
//     }
//     else{
//         alert('Insira uma resposta válida!');
//     }
// }

alert('Tem mais alguma tecnologia que gostaria de aprender? Clique em "Cancel" para sair.');
resposta4 = prompt('Digite o nome da tecnologia deseja aprender:');

let tecnologias;
while(resposta4 != undefined){
    alert(`Muito interesante ${resposta4}! Bastante promissora.`)
    resposta4 = tecnologias[i];
    i++;
    resposta4 = prompt('Digite o nome de outra tecnologia deseja aprender:');
}

alert('Obrigado por participar!');
alert(`Você escolheu ser um desenvolvedor ${resposta1}, e aprender ${resposta2}! \n Além disso, vocẽ pensa em ${resposta3}`);




