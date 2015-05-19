describe('ChickenWatch App', function () {

	describe('Chicken product list view', function() {

		beforeEach(function() {
			browser.get('poultry_app/templates/index.html');
		});

		it('should filter the chicken product list as a
			user types into the search box', function() {

			var chickenProductList = element.all(by.repeater('chickenItem in chickenProducts'));
			var query = element(by.model('query'));

			expect(chickenProductList.

				//tutorial:
				 //chicken.ProductList.count()).toBe(3)
				  //there are only 3 phones in the tutorial 
				);

			query.sendKeys(
			 // tutorial: 'nexus'
				)
			expect(
// 			tutorial: phoneList.count()).toBe(1);
				);

			query.clear();
			query.sendKeys(
// 			'motorola'
				);
			expect(
// 			phoneList.count()).toBe(2
				);
			});
	});
});