const fliesInfo = ['ID', 'Date', 'Time', 'A', 'B', 'C', 'D', 'E', 'F', 'G']; // Other data
const flies = Array.from({length: 32}, (_, i) => ((i + 1)+9).toString()); // flies measured
const tableHeaders = fliesInfo.concat(flies); // headers for the display data table

const input = document.querySelector('#id_file'); // get the input file
let data = ""; // file contents will go here

input.addEventListener('change', (e) => {
    let colsToRemove = [];
    let htmlCols = document.getElementById("id_columns")

    // create table to display the data from the upload file
    let table = document.querySelector('#displayData');
    let tableRow = document.createElement('tr');
    for (let i = 0; i < tableHeaders.length; i++){
        const header = document.createElement('th');
        header.classList.add("col-"+tableHeaders[i]);

        header.addEventListener('click', (e) => { // get the column of the clicked header and change the bg-color (toggle class)
            let classs = e.target.classList[0]
            const column = document.querySelectorAll(`.${classs}`);

            let selectedCol = classs.split("-").pop();
            if (colsToRemove.includes(selectedCol)){
                colsToRemove = colsToRemove.filter(e => e != selectedCol);
            }
            else{
                colsToRemove.push(selectedCol);
            }
            htmlCols.value = colsToRemove.toString();
            column.forEach(cell => cell.classList.toggle("greyCell"));
        });

        const headerText = document.createTextNode(tableHeaders[i]);
        header.appendChild(headerText);
        tableRow.appendChild(header);
    }
    table.appendChild(tableRow);
    
    //read file content
    const reader = new FileReader()
    reader.onload = function() {
        data = reader.result // read file and store in var
        data = data.split(/\r?\n/);
        data = data.map(item => item = item.split(/\t/));

        // date stuff 
        console.log(data[0][1]);
        console.log(data[0][2]);
        console.log(data[data.length - 2]);

        // data[0] -> first mesurment
        // data[data.length - 2] -> last mesurment

        let startDate = data[0][1] + " " + data[0][2];
        let endDate = data[data.length - 2][1] + " " + data[data.length - 2][2];

        let startDateDate = new Date(startDate);
        let endDateDate = new Date(endDate);
        startDateDate.setTime(startDateDate.getTime() + 1 * 60 * 60 * 1000);
        endDateDate.setTime(endDateDate.getTime() + 1 * 60 * 60 * 1000);


        let startDateInputwtf = document.getElementById("id_dateFrom")
        let endDateInputwtf = document.getElementById("id_dateTo")
        startDateInputwtf.value = startDateDate.toISOString().substring(0, 16);
        endDateInputwtf.value = endDateDate.toISOString().substring(0, 16);


        // end datestuff


        const tableDisplay = data.length > 1000 ? 1000 : data.length; // limit shown data to save performance (**fix this later)

        for (let i = 0; i < tableDisplay; i++){
            let contentRow = document.createElement('tr'); // create row
            for (let j = 0; j < tableHeaders.length; j++){
                const tableData = document.createElement('td'); // create table cell
                tableData.classList.add("col-"+tableHeaders[j]);
                const tableDataText = document.createTextNode(data[i][j]); // insert data from the file in the cell
                tableData.appendChild(tableDataText);
                contentRow.appendChild(tableData);
            }
            table.appendChild(contentRow);
        }
    }
    reader.readAsText(input.files[0], 'UTF-8');    
});


// TODO
// write to new parsed file depending on checkboxes
// send to django server
// return data to frontend
// plot something


