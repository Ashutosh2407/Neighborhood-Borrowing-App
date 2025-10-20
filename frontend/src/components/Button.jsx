function Button({status}){

    var bgcolor = "bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700";
    var message = "";
    switch(status) {
    case "Borrowed":
        message = "Unavailable";
        bgcolor = "bg-red-500 text-white font-bold py-2 px-4 rounded-full disabled:bg-gray-300 disabled:cursor-not-allowed";
        break;
    case "overdue":
        message = "Overdue";
        bgcolor = "bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded";
        break;
    default:
        message = "Request";
        bgcolor = "bg-gradient-to-r from-[#F06E35] to-[#F0AA2F] hover:from-[#F06E35] hover:to-[#F2614B] hover:scale-110";
}
    

    
    return (
        <div>
        <button className= {`${bgcolor} transition-all text-white px-6 py-2 rounded-full`}
        disabled = {status === "Borrowed"}>
                  {message}
        </button>
    </div>
    )
    
}

export default Button