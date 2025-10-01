let idade = 30;
console.log(idade)


function soma(num1, num2){
return num1+num2;
}
let num1 = 2
let num2 = 3 
console.log(soma(num1, num2));



function soma(a, b) {
  return a + b;
}

// Exemplo de uso:
let resultado = soma(5, 3);
console.log("A soma é:", resultado); // Saída: A soma é: 8



let num = 7; // Você pode alterar esse valor para testar outros números

if (num % 2 === 0) {
  console.log("O número é par");
} else {
  console.log("O número é ímpar");
}




for (let i = 65; i <= 90; i++) {
  console.log(String.fromCharCode(i));
}




let n1 = 8;
let n2 = 7;
let n3 = 9;

let media = (n1 + n2 + n3) / 3;

console.log("A média é:", media);




console.log("Olá, mundo!");


let num = 5;

while (num >= 1) {
  console.log(num);
  num--;
}




function calcularProduto(a, b) {
  let resultado = a * b;
  debugger; // Pausa a execução aqui
  return resultado;
}

// Chamada da função
calcularProduto(5, 10);
