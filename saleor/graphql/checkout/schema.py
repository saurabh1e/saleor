import graphene
from graphene_django.fields import DjangoConnectionField
from graphql_jwt.decorators import permission_required

from ..core.fields import PrefetchingConnectionField
from ..payment.mutations import CheckoutPaymentCreate
from .mutations import (
    CheckoutAddPromoCode,
    CheckoutBillingAddressUpdate,
    CheckoutClearStoredMeta,
    CheckoutClearStoredPrivateMeta,
    CheckoutComplete,
    CheckoutCreate,
    CheckoutCustomerAttach,
    CheckoutCustomerDetach,
    CheckoutEmailUpdate,
    CheckoutLineDelete,
    CheckoutLinesAdd,
    CheckoutLinesUpdate,
    CheckoutRemovePromoCode,
    CheckoutShippingAddressUpdate,
    CheckoutShippingMethodUpdate,
    CheckoutUpdateMeta,
    CheckoutUpdatePrivateMeta,
    CheckoutUpdateVoucher,
    CheckoutAddDeliverySchedule)
from .resolvers import resolve_checkout, resolve_checkout_lines, resolve_checkouts,\
    resolve_checkout_delivery_schedule, resolve_checkout_delivery_schedules
from .types import Checkout, CheckoutLine, CheckoutDeliverySchedule


class CheckoutQueries(graphene.ObjectType):
    checkout = graphene.Field(
        Checkout, description="Single checkout.", token=graphene.Argument(graphene.UUID)
    )
    # FIXME we could optimize the below field
    checkouts = DjangoConnectionField(Checkout, description="List of checkouts.")
    checkout_line = graphene.Field(
        CheckoutLine,
        id=graphene.Argument(graphene.ID),
        description="Single checkout line.",
    )
    checkout_lines = PrefetchingConnectionField(
        CheckoutLine, description="List of checkout lines"
    )

    checkout_delivery_schedule = graphene.Field(
        CheckoutDeliverySchedule,
        id=graphene.Argument(graphene.ID),
        description="Single checkout line.",
    )
    checkout_delivery_schedules = PrefetchingConnectionField(
        CheckoutDeliverySchedule, description="List of checkout lines"
    )

    def resolve_checkout(self, *_args, token):
        return resolve_checkout(token)

    @permission_required("order.manage_orders")
    def resolve_checkouts(self, *_args, **_kwargs):
        resolve_checkouts()

    def resolve_checkout_line(self, info, id):
        return graphene.Node.get_node_from_global_id(info, id, CheckoutLine)

    @permission_required("order.manage_orders")
    def resolve_checkout_lines(self, *_args, **_kwargs):
        return resolve_checkout_lines()

    def resolve_checkout_delivery_schedule(self, info, id):
        return graphene.Node.get_node_from_global_id(info, id, CheckoutDeliverySchedule)

    # @permission_required("order.manage_orders")
    def resolve_checkout_delivery_schedules(self, *_args, **_kwargs):
        return resolve_checkout_delivery_schedules()


class CheckoutMutations(graphene.ObjectType):
    checkout_add_promo_code = CheckoutAddPromoCode.Field()
    checkout_billing_address_update = CheckoutBillingAddressUpdate.Field()
    checkout_complete = CheckoutComplete.Field()
    checkout_create = CheckoutCreate.Field()
    checkout_customer_attach = CheckoutCustomerAttach.Field()
    checkout_customer_detach = CheckoutCustomerDetach.Field()
    checkout_email_update = CheckoutEmailUpdate.Field()
    checkout_line_delete = CheckoutLineDelete.Field()
    checkout_lines_add = CheckoutLinesAdd.Field()
    checkout_lines_update = CheckoutLinesUpdate.Field()
    checkout_remove_promo_code = CheckoutRemovePromoCode.Field()
    checkout_payment_create = CheckoutPaymentCreate.Field()
    checkout_shipping_address_update = CheckoutShippingAddressUpdate.Field()
    checkout_shipping_method_update = CheckoutShippingMethodUpdate.Field()
    checkout_update_voucher = CheckoutUpdateVoucher.Field()
    checkout_update_metadata = CheckoutUpdateMeta.Field()
    checkout_clear_metadata = CheckoutClearStoredMeta.Field()
    checkout_update_private_metadata = CheckoutUpdatePrivateMeta.Field()
    checkout_clear_private_metadata = CheckoutClearStoredPrivateMeta.Field()
    checkout_add_delivery_schedule = CheckoutAddDeliverySchedule.Field()

