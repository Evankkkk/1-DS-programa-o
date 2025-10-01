// Cria array chamado 'turma' com objetos que representam alunos e suas notas
let turma = [
{ nome: "João", nota: 7 },
{ nome: "Maria", nota: 9 },
{ nome: "Pedro", nota: 6 }
];

// Laço for Percorre o array 'turma' para a impresão formatada de dados na tela
for (let i = 0; i < turma.length; i++) {
console.log(turma[i].nome + ": " + turma[i].nota);
}

// Laço para somar e calcular media
let soma = 0;
for (let i = 0; i < turma.length; i++) {
soma += turma[i].nota;
}
let media = soma / turma.length;
console.log("Média da turma: " + media);

// Laço for com estrutura condicional
for (let aluno of turma) {
  if (aluno.nota >= 7) {
    console.log(aluno.nome + " está aprovado");
  } else {
    console.log(aluno.nome + " está reprovado");
  }
}

// Cria um objeto 'aluno' com nome e um array de notas
let aluno = {
nome: "Lucas",
notas: [7, 8, 9]
};
// Inicializa a variável 'total' para acumular as notas
let total = 0;
// Percorre o array de notas e soma cada valor à variável 'total'
for (let nota of aluno.notas) {
total += nota;
}
// Calcula a média dividindo o total pela quantidade de notas
console.log("Média: " + (total / aluno.notas.length));

