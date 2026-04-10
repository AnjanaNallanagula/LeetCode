/**
 * @param {number} n
 * @return {Function} counter
 */

var createCounter = function(n) {
    var count = 0;
    
    return function() {
        console.log(count)

        var d = n + count;
        count++;

        return d
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */