import { PhotoIcon, UserCircleIcon } from '@heroicons/react/24/solid'
import { ChevronDownIcon } from '@heroicons/react/16/solid'
import api from '../api';
import { Navigate, useNavigate } from 'react-router-dom';



function ItemForm() {

    const navigate = useNavigate();
    const handleSubmit = async (e) => {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        
        const data = {

            description: formData.get('description'),
            item_name: formData.get('item_name'),
            due_date: formData.get('due_date') || null,
            status: formData.get('status'),
        
        };

        try {
            const response = await api.post('item/create/', data);
            console.log('Success:', response.data);
            navigate("/");
            
        } catch (error){
            console.log('Full error:', error);
            console.log('Error response:', error.response);
            console.log('Error data:', error.response?.data);
        }
    };



    
    return (
        <div className='m-8 p-10'>
            <form onSubmit={handleSubmit}>
                <div className="space-y-12">
                    <div className="border-b border-gray-900/10 pb-12">
                        <h1 className="text-base/7 font-semibold text-gray-900">Item</h1>
                        <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">

                            <div className="col-span-full">
                                <label htmlFor="description" className="block text-sm/6 font-medium text-gray-900">
                                    Description
                                </label>
                                <div className="mt-2">
                                    <textarea
                                        id="description"
                                        name="description"
                                        rows={3}
                                        className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                                        defaultValue={''}
                                        placeholder = "Describe the item in a few sentences."
                                    />
                                </div>
                                
                            </div>

                            <div className="col-span-full">
                                <label htmlFor="photo" className="block text-sm/6 font-medium text-gray-900">
                                    Item Photo
                                </label>
                                <div className="mt-2 flex items-center gap-x-3">
                                    <UserCircleIcon aria-hidden="true" className="size-12 text-gray-300" />
                                    <button
                                        type="button"
                                        className="rounded-md bg-white px-2.5 py-1.5 text-sm font-semibold text-gray-900 shadow-xs ring-1 ring-gray-300 ring-inset hover:bg-gray-50"
                                    >
                                        Upload
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="border-b border-gray-900/10 pb-12">
                        <h2 className="text-base/7 font-semibold text-gray-900">Item Information</h2>
                        <div className="mt-10 grid grid-cols-1 gap-x-6 gap-y-8 sm:grid-cols-6">
                            <div className="sm:col-span-3">
                                <label htmlFor="first-name" className="block text-sm/6 font-medium text-gray-900">
                                    Item Name
                                </label>
                                <div className="mt-2">
                                    <input
                                        id="item-name"
                                        name="item_name"
                                        type="text"
                                        autoComplete="group-name"
                                        className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                                    />
                                </div>
                            </div>

                            <div className="sm:col-span-3">
                                <label htmlFor="due-date" className="block text-sm/6 font-medium text-gray-900">
                                    Due Date
                                </label>
                                <div className="mt-2">
                                    <input
                                        id="due-date"
                                        name="due_date"
                                        type="date"
                                        autoComplete="due-date"
                                        className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                                    />
                                </div>
                            </div>

                            

                            <div className="sm:col-span-3">
                                <label htmlFor="status" className="block text-sm/6 font-medium text-gray-900">
                                    Status
                                </label>
                                <div className="mt-2 grid grid-cols-1">
                                    <select
                                        id="status"
                                        name="status"
                                        autoComplete="status-name"
                                        className="col-start-1 row-start-1 w-full appearance-none rounded-md bg-white py-1.5 pr-8 pl-3 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                                    >
                                        <option>Available</option>
                                        <option>Requested</option>
                                        <option>Borrowed</option>
                                        <option>Overdue</option>
                                    </select>
                                    <ChevronDownIcon
                                        aria-hidden="true"
                                        className="pointer-events-none col-start-1 row-start-1 mr-2 size-5 self-center justify-self-end text-gray-500 sm:size-4"
                                    />
                                </div>
                            </div>

                            

                            {/* <div className="sm:col-span-2 sm:col-start-1">
                                <label htmlFor="city" className="block text-sm/6 font-medium text-gray-900">
                                    City
                                </label>
                                <div className="mt-2">
                                    <input
                                        id="city"
                                        name="city"
                                        type="text"
                                        autoComplete="address-level2"
                                        className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                                    />
                                </div>
                            </div> */}

                            {/* <div className="sm:col-span-2">
                                <label htmlFor="state" className="block text-sm/6 font-medium text-gray-900">
                                    State / Province
                                </label>
                                <div className="mt-2">
                                    <input
                                        id="state"
                                        name="state"
                                        type="text"
                                        autoComplete="address-level1"
                                        className="block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6"
                                    />
                                </div>
                            </div> */}

                            
                        </div>
                    </div>

                    
                </div>

                <div className="mt-6 flex items-center justify-end gap-x-6">
                    <button type="button" className="text-sm/6 font-semibold text-gray-900">
                        Cancel
                    </button>
                    <button
                        type="submit"
                        className="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-xs hover:bg-indigo-500 focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
                        
                    >
                        Submit
                    </button>
                </div>
            </form>

        </div>

    )
}

export default ItemForm