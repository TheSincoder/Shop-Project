from . import bp as api
from.forms import ItemForm
from app.blueprints.auth.auth import token_auth
from flask import request, make_response, g, abort
# from app.helpers import require_admin
from flask import render_template, request, flash, redirect, url_for
from app.models import Item, Cart, User, db
from flask_login import current_user, login_required

# name
# price
# desc
# img

# Create Item
@api.route('/create_item', methods = ['GET', 'POST'])

def create_item():
    form = ItemForm()
    if request.method == 'POST' and form.validate_on_submit():
        # Create a new item
        try:
            new_item_data = {
                "name":form.name.data.title(),
                "price":form.price.data,
                "desc":form.desc.data,
                "img":form.img.data,
            }
            #create an empty User
            new_item_object = Item()
            #build user with form data
            new_item_object.from_dict(new_item_data)
            #save user to the database
            new_item_object.save()
        except:
            flash('There was an unexpected ERROR creating your Account. Please Try Again', 'danger')
            #Error Return
            return render_template('create_item.html.j2', form=form)
        # If it worked
        flash('You have registered successfully created the item', 'warning')
        return redirect(url_for('api.view_shop'))
        
    #GET Return
    return render_template('create_item.html.j2', form = form)

# View Shop
@api.route('/view_shop', methods=['GET'])
@login_required
def view_shop():
    # access the items
    # display each item on the page

    items = Item.query.all()
    return render_template('view_shop.html.j2', items = items)

# Add to cart

@api.route('/add_to_cart/<int:id>')
@login_required
def add_to_cart(id):
    # make id = the specific item i'm clicking on
    item = Item.query.get((id))    
    current_user.user_item.append(item)
    db.session.commit()
    flash(f'You have added {item.name} to your cart', 'warning')
    
    return redirect(url_for('api.view_shop'))

# Remove from cart

@api.route('/remove_from_cart/<int:id>')
@login_required
def remove_from_cart(id):
    # make id = the specific item i'm clicking on
    item = Item.query.get((id))
    print(item)
    current_user.user_item.remove(item)
    db.session.commit()
    flash(f'You have removed that item from your cart', 'warning')
    return redirect(url_for('api.cart'))

# remove all items
@api.route('/remove_all_items')
@login_required
def remove_all_items():    
    
    items = Cart.query.filter_by(user_id = current_user.id).all()
    for item in items:
        print(item)
        Cart.delete(item)
         
    db.session.commit()
    flash(f'You have removed all the items from your cart', 'warning')
    return redirect(url_for('api.cart'))

# View Cart

@api.route('/cart', methods=['GET'])
@login_required
def cart(): 
    items = current_user.user_item
    return render_template('cart.html.j2', items = items)

# View Item Details
@api.route('/item/<int:id>')
@login_required
def get_item(id):
    item = Item.query.get(id)
    return render_template('single_item.html.j2', item=item)