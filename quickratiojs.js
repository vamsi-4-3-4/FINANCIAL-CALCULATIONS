//currentassets=600000000;
//inventories=100000000;
//currentliabilities=900000000;


const quickratio=(currentassets,inventories,currentliabilities)=>{
    try{
        var quickratio=(currentassets-inventories)/currentliabilities;
        console.log(quickratio)
    }
    catch(error){
        console.error(error);
    }
};

quickratio(600000000,100000000,900000000);

