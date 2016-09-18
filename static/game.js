    window.onload = function()
    {
        var canvas = document.createElement('canvas'),
        ctx = canvas.getContext('2d'),
        score = 0;
     
        // Initialize the matrix.
     
        canvas.width = 300;
        canvas.height = 300;
     
        var body = document.getElementsByTagName('body')[0];
        body.appendChild(canvas);
     
        // Add the snake
        map = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 1], [0, 0, 0, 0, 1], [1, 1, 1, 1, 1]];
     
        drawGame();
     
        function drawGame() 
	    {
	        // Clear the canvas
	        ctx.clearRect(0, 0, canvas.width, canvas.height);
	     
	            
	        // Draw the border as well as the score
	        drawMain();
	     
	        // Start cycling the matrix
	        for (var x = 0; x < map.length; x++) {
	            for (var y = 0; y < map[0].length; y++) {
	                if (map[x][y] === 1) {
	                    ctx.fillStyle = 'black';
	                    ctx.fillRect(x * 60, y * 60 + 20, 60, 60);
	                } else if (map[x][y] === 0) {
	                    ctx.fillStyle = 'orange';
	                    ctx.fillRect(x * 60, y * 60 + 20, 60, 60);          
	                }
	            }
	        }
	        
	        if (active) {
	            // Call the drawGame() function
	        }
	    }
     
     
        function drawMain() 
        {
            ctx.lineWidth = 2; // Our border will have a thickness of 2 pixels
            ctx.strokeStyle = 'black'; // The border will also be black
     
            // The border is drawn on the outside of the rectangle, so we'll
            // need to move it a bit to the right and up. Also, we'll need
            // to leave a 20 pixels space on the top to draw the interface.
            ctx.strokeRect(2, 20, canvas.width - 4, canvas.height - 24);
     
            ctx.font = '12px sans-serif';
            ctx.fillText('Score: ' + score, 2, 12);
        }
     
     
        
    };