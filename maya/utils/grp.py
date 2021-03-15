global proc grp (string $argList){
    // set default
    int $worldCenter = false;
    
    // argument list
    string $argData[];
    
    // Seprate space-delimited arguments into argument array
    tokenize $argList " " $argData;
    
    for ($arg in $argData){
        switch ($arg){
            // center pivot the group
            case "-w":
            $worldCenter = true;
            break;
        }
    }
    
    string $name = $argData[0];

    
    // Center Pivot
    if ($worldCenter){
        doGroup 0 1 1;
    } else{
    // Group selection
    group -n $name;
    
    }
}