import Itemfilter from "../components/Itemfilter";
import Navbar from "../components/Navbar";

function MyItems(){
    return (
        <div>
        <Navbar />

        <Itemfilter heading = {"My Items"}   />
        </div>
    )
}

export default MyItems