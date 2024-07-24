// Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

function problem(x){
    if(isNaN(x) || x === "")
    {
        console.log("Error")
        return "Error";
    }
    else
    {
        let total = (x*50) + 6;
        console.log("Here is my total: " + total);
        return (x*50)+6;
    }
}
problem(0);

// Best Practice:
// const problem = x => typeof x === 'string' ? 'Error' : x * 50 + 6;