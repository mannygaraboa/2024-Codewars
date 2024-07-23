// Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

function problem(x){
    let total = [(x*50) + 6];
    if(total == NaN)
    {
        console.log("This is a string");
        return Error;
    }
    console.log("Here is my total: " + total);

    return 0;
}
problem("4");