function Item({item}) {
  return (
    <div>
      {/* <div class="bg-gradient-to-br from-blue-50 to-indigo-100 min-h-screen p-6">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"> */}
          <div class="bg-white/70 backdrop-blur-sm rounded-2xl p-6 shadow-xl hover:shadow-2xl transition-all duration-300 hover:-translate-y-1">
            <div class="relative">
              <img src="item.jpg" alt="Item" class="w-full h-40 object-cover rounded-xl" />
              <div class="absolute top-3 right-3">
                <span class="bg-green-500 text-white px-2 py-1 rounded-full text-xs font-medium">
                  Available
                </span>
              </div>
            </div>
            <div class="mt-4">
              <h3 class="text-xl font-bold text-gray-900">{item.item_name}</h3>
              <p class="text-gray-600 mt-1">{item.item_description}</p>
              <div class="flex items-center justify-between mt-6">
                <div class="text-sm text-gray-500">
                  <p>Owner: {item.owner}</p>
                  <p>Max: 3 days</p>
                </div>
                <button class="bg-gradient-to-r from-blue-500 to-purple-600 text-white px-6 py-2 rounded-full hover:from-blue-600 hover:to-purple-700 transition-all">
                  Request
                </button>
              </div>
            </div>
          </div>
        </div>


    //   </div>

    // </div>

  )
}

export default Item


