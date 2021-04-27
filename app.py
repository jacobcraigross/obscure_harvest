// test arrays
const alphaArrayFour = ["hello", "world", "hello", "again", "texas", "hello", "insane", "hello", "hello"];

const occStr = "death is born from killers. we kill with the killers and we drink their blood. along the way, killers have spread death! killers have plundered. we are the dead killers?!! if the sun rises, you know we are the blood drenched killers from hell... we are awaiting a horrible death, one that is fit for barbaric hellish (killers)";

//problem one.... sort the numbers accurately, ascending and descending. 
// ascending solution 1 ..... a - b
const ascNums = (array) => {
    if(!array.length) return;
    return array.sort((a, b) => a - b);
}
// descending solution 1 ..... a - b.reverse()
const descNums = (array) => {
    if(!array.length) return;
    return array.sort((a, b) => a - b).reverse();
}
// descending solution 2 ..... b - a
const descNumsTwo = (array) => {
    if(!array.length) return;
    return array.sort((a, b) => b - a);
}
console.log(ascNums(alphaArrayThree));
console.log(descNumsTwo(alphaArrayThree));
console.log(descNums(alphaArrayThree));

//sort an array of numbers and strings. 
const numsAndStrings = (array) => {
    if(!array.length) return;
    const strArray = [];
    const numArray = [];
    array.forEach(element => {
        isNaN(element) ? strArray.push(element) : numArray.push(element);
    });
    // by default sort will alphabetize strings. 
    strArray.sort();
    numArray.sort((a, b) => a - b);
    return [...numArray, ...strArray];
}
console.log(numsAndStrings(alphaArrayTwo));


//define a function that takes in an array of nums and strs and returns the most commonly occuring STRING. 

// E6 answer which is more modern and readable. *** But doesnt allow for ties ***
const mostCommonStr = (array) => {
    if(!array.length) return;
    const arr = [...array];
    return arr.sort((a, b) => arr.filter(str => str === a).length - arr.filter(str => str === b).length).pop();
}

console.log(mostCommonStr(alphaArrayFour));


// a way that accounts for ties. BUT object keys always convert nums to strings, just an FYI. They still get counted, but they'll be converted. 
const mostCommonElement = (array) => {
    if(!array.length) return; // if its an empty array, return statement to break out of the function. 
    const counterObject = {}; // create a counter object to house the iterative data from the initial array
    array.forEach(element => { // loop over each item in the array and if it exists, give it a count by 1. (keeps running total of the key [0] and value/count [1])
        counterObject[element] ? counterObject[element] += 1 : counterObject[element] = 1;
    });
    const sortedArray = [];
    Object.keys(counterObject).forEach(key => {
        sortedArray.push( [key, counterObject[key]] );
    });
    sortedArray.sort((a, b) => a[1] - b[1]);
    const maxCount = sortedArray[sortedArray.length - 1][1];
    const resultArray = []; // just prints the element, no count. 
    sortedArray.forEach(arr => {
        if(arr[1] === maxCount) {
            resultArray.push(arr[0]);
        }
    });
    return resultArray;
}
console.log(mostCommonElement(alphaArrayFour));

const resultArray = sortedArray.filter(arr => arr[1] === maxCount);

// count occurences of every word in the string. REGEX NIGHTMARE
const countAllWords = (string) => {
    if(!string.length) return;
    const wordArray = string.toLowerCase().replace(/([.!?,:;@+=~|"'><^%&()])/g, '').replace(/[\s]{2,}/g, ' ').split(' ');
    const counterObject = {};
    wordArray.forEach(word => {
        counterObject[word] ? counterObject[word] += 1 : counterObject[word] = 1;
    });

    return counterObject;
}
console.log(countAllWords(occStr));

// only return the HIGHEST OCCURING WORD. 
const highestWord = (string) => {
    if(!string.length) return;
    const highestWordArray = string.toLowerCase().replace(/([.!?,:;@+=~|"'><^%&()])/g, '').replace(/[\s]{2,}/g, ' ').split(' ');
    return mostCommonElement(highestWordArray);
}
console.log(highestWord(occStr));

