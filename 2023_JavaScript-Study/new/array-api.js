
// Q1. make a string out of an array
{
    const fruits = ['apple', 'banana', 'orange'];
    // const result = fruits.toString();
    const result = fruits.join();
    console.log(result);
}
  
  // Q2. make an array out of a string
  {
    const fruits = '🍎, 🥝, 🍌, 🍒';
    const result = fruits.split(',');
    console.log(result);
  }
  
  // Q3. make this array look like this: [5, 4, 3, 2, 1]
  {
    const array = [1, 2, 3, 4, 5];
    const result = array.reverse(); // mutate
    console.log(result);
  }
  
  // Q4. make new array without the first two elements
  {
    const array = [1, 2, 3, 4, 5];
    const result = array.slice(2,);
    console.log(result);
  }
  
  class Student {
    constructor(name, age, enrolled, score) {
      this.name = name;
      this.age = age;
      this.enrolled = enrolled;
      this.score = score;
    }
  }
  const students = [
    new Student('A', 29, true, 45),
    new Student('B', 28, false, 80),
    new Student('C', 30, true, 90),
    new Student('D', 40, false, 66),
    new Student('E', 18, true, 88),
  ];
  
  // Q5. find a student with the score 90
  {
    // students.forEach((obj) => {
    //     if (obj.score >= 90) console.log(obj.name);
    // })

    const result = students.find((obj) => obj.score === 90)
    console.log(result);
  }
  
  // Q6. make an array of enrolled students
  {
    // const result = [];
    // students.forEach((obj) => {
    //     if (obj.enrolled === true) result.push(obj);
    // })
    // console.log(result);
    const result = students.filter((obj) => obj.enrolled);
    console.log(result);
  }
  
  // Q7. make an array containing only the students' scores
  // result should be: [45, 80, 90, 66, 88]
  {
    // const result = [];
    // students.forEach((obj) => {
    //     result.push(obj.score);
    // })
    // console.log(result);
    const result = students.map((obj) => obj.score);
    console.log(result);
  }
  
  // Q8. check if there is a student with the score lower than 50
  {
    console.log(students.some((obj) => obj.score < 50));
  }
  
  // Q9. compute students' average score
  {
    // let avg = 0;
    // students.forEach((obj) => {
    //     avg += obj.score;
    // })
    // const result = avg / students.length;
    // console.log(result);
    let result = students.reduce((prev, curr) => prev+curr.score, 0);
    result = result / students.length;
    console.log(result);
  }
  
  // Q10. make a string containing all the scores
  // result should be: '45, 80, 90, 66, 88'
  {
    // const temp = [];
    // students.forEach((obj) => {
    //     temp.push(obj.score);
    // })
    // const result = temp.toString()
    // console.log(result);

    const result = students.map((obj) => obj.score).join();
    console.log(result);
  }
  
  // Bonus! do Q10 sorted in ascending order
  // result should be: '45, 66, 80, 88, 90'
  {
    // const temp = [];
    // students.forEach((obj) => {
    //     temp.push(obj.score);
    // })
    // const result = temp.sort().toString();
    // console.log(result);

    const result = students.map((obj) => obj.score).sort().join();
    console.log(result);
  }
//   array-api.js
//   array-api.js 표시 중입니다.