alert("Funciones recursivas")
text = "Que tal"
alert("Ejercicio 1")
function stringInvertido(texto) {
    return texto.reverse(" ");
}

alert (text)
let reverseString = reverse(text)
alert (reverseString)
alert("Ejercicio2")

var limit = 15;
	var fibonacci = [0,1];

	for(i=2; i <= limit; i++){
		fibonacci.push(fibonacci[i-1] + fibonacci[i-2]);
}
alert(fibonacci)

alert("Ejercicio 3")
number = "12345"
function reverse (number) {
    if (number === "") {
        return " ";
    } else {
        return reverse(number.substr(1)) + number.charAt(0);
    }
}

let reversednumber = reverse(number)
alert(number)
alert(reversednumber)



alert("Ejercicio4")
alert("5^3")
var elevar = (5 ** 3)
alert(elevar)


alert("Ejercicio5")

let numeros = [1, 9]
alert("rango[1,9]")

function suma_todos (numeros) {
  let inicio = numeros[0];
  let fin = numeros[1];
  let suma = 0;
  
  for (let i = inicio; i <= fin; i++) {
    suma += i;
  }
  
  return suma;
}
alert("Ejercicio6")

alert(suma_todos(numeros))

function palindromo(texto) {
    return texto.split('').reverse().join('') == texto;
}

alert("La palabra oso es palindroma?", palindromo("oso"));

alert("Ejercicio7");

function suma(numeros) {
  if(numeros==1){
    return 1;

  }else{
    return numeros + suma(numeros -1)

  }
}

resultado_suma = suma(6)
print(resultado_suma);

print("Ejercicio9")
function BinADeci(binario) {
  if(binario.constructor !=string) {
    return null;
  }
  binario = binario.replace(/[^01]/gi,'');
  return Number.parseInt(binario, 2);

}

alert(BinADeci('1001'));

alert("Ejercicio10");

function elementoAleatorio(datos) {
  if (!Array.isArray(datos)) {
      throw TypeError('El argumento debe ser un arreglo.');
  }

  if (!datos.length) {
      return null;
  }

  let indiceAleatorio = Math.floor(Math.random() * datos.length);

  return datos[indiceAleatorio];
}
  alert(elementoAleatorio([1,2,3,4,5]));



