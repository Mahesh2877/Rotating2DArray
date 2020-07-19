Problem Statement - To rotate a given square matrix clockwise by 90 degrees.

The solution can be of two types -> In-place and Out-of-place.

In Place Solution -
Here, we are not allowed to create a separate matrix. We have to edit the contents of the original matrix. As a result, this involves moving values of one cell(say, A) to  another cell(say, B), while moving the original value of cell B to cell C.

We split the matrix into four parts, the upper left, upper right, lower left and lower right portions. This can sometimes(if the matrix has an odd number of rows and columns) leave out the middle cell which will not change values during the rotation.
If the matrix has odd number of rows, then these four parts will be rectangular portions. For even numbered rows and columns, these portions will be square-shaped portions.

Once, we have identified the four portions of the matrix, rotating it is nothing but rotating each portion, and moving it to the next portion. Example - rotate the upper left portion by clockwise 90 degrees, and move it to the upper right portion, while rotating the original upper right portion clockwise and moving it to the lower right portion, etc.

Since the size of the four individual portions will be the same, we only need to loop through the contents of the upper-left portion. Example - The upper left portion will include the cell (0, 0). We store it's value(say, A). Then we find the new location where this value 'A' should go to. We then store the value of that cell(say, B) as well. This way, we'll get four values(A, B, C, D) for the four corners of the matrix. We simply need to iterate through this loop to apply the values to the new cells. Once this is done, we have successfully updated the cells corresponding to one of the cells of the upper-left portion of the matrix.

We repeat the step in the above paragraph but for the next cell in the upper-left portion.
