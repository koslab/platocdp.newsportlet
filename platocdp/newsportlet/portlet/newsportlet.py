from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form

# XXX: Uncomment for z3cform

from z3c.form import field

from plone.formwidget.contenttree import ObjPathSourceBinder
from z3c.relationfield.schema import RelationList, RelationChoice

from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.cache import render_cachekey

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from platocdp.newsportlet import MessageFactory as _

from plone.portlet.collection import collection
from plone.app.form.widgets.uberselectionwidget import UberSelectionWidget

class INewsPortlet(collection.ICollectionPortlet):
    """
    Define your portlet schema here
    """
    pass

class Assignment(base.Assignment):
    implements(INewsPortlet)

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def title(self):
        return _('News Portlet')

class Renderer(collection.Renderer):
    
    render = ViewPageTemplateFile('templates/newsportlet.pt')

    @property
    def available(self):
        return True

class AddForm(collection.AddForm):

    form_fields = form.Fields(INewsPortlet)
    form_fields['target_collection'].custom_widget = UberSelectionWidget
    # hide these fields from collectionportlet, we dont need these here
    form_fields = form_fields.omit('random', 'show_more', 'show_dates')


    label = _(u"Add News Portlet")
    description = _(u"Basic news portlet with image")

    def create(self, data):
        return Assignment(**data)

class EditForm(collection.EditForm):

    form_fields = form.Fields(INewsPortlet)
    form_fields['target_collection'].custom_widget = UberSelectionWidget
    # hide these fields from collectionportlet, we dont need these here
    form_fields = form_fields.omit('random', 'show_more', 'show_dates')


    label = _(u"Edit News Portlet")
    description = _(u"Basic news portlet with image")
