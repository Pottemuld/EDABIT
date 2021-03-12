function intWithinBounds(test, lower, upper) {
    if(Number.isInteger(test) && Number.isInteger(lower) && Number.isInteger(upper)) {
        if(lower < test && test < upper) {
            console.log("true");
        }
        else {console.log("false");}
    } else {console.log("false");}
}


intWithinBounds(3, 1, 9);
intWithinBounds(6, 1, 6);
intWithinBounds(4.5, 3, 8);