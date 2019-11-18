// let(변수)
let x = 1
// let x = 3
// x = 3 // 재할당 가능
// console.log(x)

if (x === 1){
  let x = 2
  console.log(x) // 2
}
console.log(x) // 1

// const (상수)
// 초기값 생략하면 error
// const MY_FAV
// MY_FAV를 상수로 정의하고 그 값을 7로 함.
const MY_FAV = 7
// console.log('My Favorite number is ... ' + MY_FAV)
// 상수 재할당 에러 -> Assignment
// MY_FAV = 10
// 상수 재선언 에러 -> already been declared
const MY_FAV = 20
let MY_FAV = 11

if (MY_FAV === 7) {
  const MY_FAV = 11
  console.log(MY_FAV)
}
console.log(MY_FAV)