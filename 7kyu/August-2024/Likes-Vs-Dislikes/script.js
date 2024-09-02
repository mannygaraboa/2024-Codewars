// Like, Dislike, Nothing come from Preloaded

function likeOrDislike(buttons) {
    console.log(buttons)
    let status = 0;

    if(!buttons) {
        return "Nothing"
    }
    else {
        for(let i = 0; i < buttons.length; i++) {
            if(buttons[i] === "Like") {
                if(status == 0 || status == -1) {
                    status = 1;
                }
                else if(status == 1) {
                    status = 0;
                }
            }
            else if(buttons[i] === "Dislike") {
                if(status == 0 || status == 1) {
                    status = -1;
                }
                else if(status == -1) {
                    status = 0;
                }
            }
        }
    }

    if(status == 0) {
        console.log("Nothing");
        return "Nothing";
    }
    else if(status == 1) {
        console.log("Like");
        return "Like";
    }
    else if(status == -1) {
        console.log("Dislike");
        return "Dislike";
    }
}
likeOrDislike([]);

// Best Practice:
    // function likeOrDislike(buttons) {
    //     let state = 'Nothing';
    
    //     for (let i = 0; i < buttons.length; i++) {
    //       if (buttons[i] === state) {
    //         state = 'Nothing'
    //       } else {
    //         state = buttons[i]
    //       }
    //     }
    
    //     return state
    // }