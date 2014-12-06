improve = function improve(positions,path,once){
    // WARNING: MUTABILIDADE
    // Modifica caminho in-place para performance.
    // Otimizado, mas estúpido, pois modifica um
    // cruzamento e retorna. Seria melhor se modificasse
    // todos os cruzamentos de uma vez (ou seja, não
    // retornando...).
    //
    //     e f crosses with j k
    //
    //     --e j--       --e-j--
    //        X   |  ->         |
    //     --k f--       --k-f--
    //
    //         i         j  
    // 0 1 2 3 4 5 6 7 8 9 A B C D E
    // a b c d e f g h i j k l m n o
    //           |reverse|
    // a b c d e j i h g f k l m n o
    for (var i=0, l=path.length; i<l-2; ++i){
        for (var j=i+2; j<l-1; ++j){
            // Essa suruba matematica usa produtos vetoriais para 
            // checar se 2 segmentos se cruzam. Tudo é inlined,
            // para performance.
            var a = positions[path[i]];
            var b = positions[path[i+1]];
            var c = positions[path[j]];
            var d = positions[path[j+1]];
            var ax = a.x, ay = a.y; 
            var bx = b.x, by = b.y; 
            var cx = c.x, cy = c.y; 
            var dx = d.x, dy = d.y;
            var aSide = (dx - cx) * (ay - cy) - (dy - cy) * (ax - cx) > 0;
            var bSide = (dx - cx) * (by - cy) - (dy - cy) * (bx - cx) > 0;
            var cSide = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax) > 0;
            var dSide = (bx - ax) * (dy - ay) - (by - ay) * (dx - ax) > 0;
            var intersects = aSide !== bSide && cSide !== dSide;
            if (intersects){
                for (var k=0; k<Math.floor((j-i)/2); ++k){
                    var tmp = path[i+1+k];
                    path[i+1+k] = path[j-k];
                    path[j-k] = tmp;
                };
                if (once) return 1;
            };
        };
    };
    return 0;
};
