"""Stream type classes for tap-ticketmatic."""

from singer_sdk import typing as th
from tap_ticketmatic.client import TicketmaticStream
from typing import Any, Dict, Optional


class Orders(TicketmaticStream):
    """Fetches the orders from Ticketmatic."""
    name = "orders"
    path = "/orders"
    primary_keys = ["orderid"]
    replication_key = "lastupdatets"

    schema = th.PropertiesList(
        th.Property("orderid", th.IntegerType),
        th.Property("amountpaid", th.NumberType),
        th.Property("calculate_ordercosts", th.BooleanType),
        th.Property("code", th.StringType),
        th.Property("customerid", th.IntegerType),
        th.Property(
            "deferredpaymentproperties",
            th.ObjectType(
                th.Property("bankAccount", th.StringType),
                th.Property("bankBic", th.StringType),
                th.Property("bankName", th.StringType),
                th.Property("transferReference", th.StringType),
            ),
        ),
        th.Property(
            "deliveryaddress",
            th.ObjectType(
                th.Property("city", th.StringType),
                th.Property("street1", th.StringType),
            ),
        ),
        th.Property("deliveryscenarioid", th.IntegerType),
        th.Property("deliverystatus", th.IntegerType),
        th.Property("expiryhandled", th.BooleanType),
        th.Property("expiryts", th.DateTimeType),
        th.Property("firstname", th.StringType),
        th.Property("hasopenpaymentrequest", th.BooleanType),
        th.Property("isauthenticatedcustomer", th.BooleanType),
        th.Property("lastname", th.StringType),
        th.Property("lookup", th.ArrayType(th.StringType)),
        th.Property("nbroftickets", th.IntegerType),
        th.Property(
            "ordercosts",
            th.ArrayType(
                th.ObjectType(
                    th.Property("orderid", th.IntegerType),
                    th.Property("amount", th.NumberType),
                    th.Property("servicechargedefinitionid", th.IntegerType),
                )
            ),
        ),
        th.Property(
            "payments",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("orderid", th.IntegerType),
                    th.Property("amount", th.NumberType),
                    th.Property("paidts", th.DateTimeType),
                    th.Property("paymentmethodid", th.IntegerType),
                    th.Property("properties", th.ObjectType()),
                    th.Property("refundpaymentid", th.IntegerType),
                )
            ),
        ),
        th.Property("paymentscenarioid", th.IntegerType),
        th.Property("paymentstatus", th.IntegerType),
        th.Property(
            "products",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("orderid", th.IntegerType),
                    th.Property("code", th.StringType),
                    th.Property("contactid", th.IntegerType),
                    th.Property("price", th.NumberType),
                    th.Property("productid", th.IntegerType),
                    th.Property("properties", th.ObjectType()),
                )
            ),
        ),
        th.Property("promocodes", th.ArrayType(th.StringType)),
        th.Property("queuetokens", th.ArrayType(th.IntegerType)),
        th.Property("rappelhandled", th.BooleanType),
        th.Property("rappelts", th.DateTimeType),
        th.Property("saleschannelid", th.IntegerType),
        th.Property("status", th.IntegerType),
        th.Property(
            "tickets",
            th.ArrayType(
                th.ObjectType(
                    th.Property("orderid", th.IntegerType),
                    th.Property("id", th.IntegerType),
                    th.Property("tickettypeid", th.IntegerType),
                    th.Property("seatzoneid", th.IntegerType),
                    th.Property("seated_ref", th.StringType),
                    th.Property("price", th.NumberType),
                    th.Property("tickettypepriceid", th.IntegerType),
                    th.Property("servicecharge", th.NumberType),
                    th.Property("ticketholderid", th.IntegerType),
                    th.Property("ticketname", th.StringType),
                    th.Property("vouchercodeid", th.IntegerType),
                    th.Property("bundleid", th.IntegerType),
                    th.Property("barcode", th.StringType),
                    th.Property("deliveredts", th.StringType),
                    th.Property("transferredto", th.StringType),
                    th.Property("cachedaccesscontrolstatus", th.IntegerType),
                    th.Property("eventid", th.IntegerType),
                    th.Property("pricetypeid", th.IntegerType),
                    th.Property("seatdescription", th.StringType),
                    th.Property("seatname", th.StringType),
                    th.Property("seatcachedvisualx", th.NumberType),
                    th.Property("seatcachedvisualy", th.NumberType),
                    th.Property("tickettypename", th.StringType),
                    th.Property("bundlevariant", th.StringType),
                )
            ),
        ),
        th.Property("totalamount", th.NumberType),
        th.Property("webskinid", th.IntegerType),
        th.Property("createdts", th.DateTimeType),
        th.Property("lastupdatets", th.DateTimeType),
        th.Property("c_remark", th.StringType),
        th.Property("c_podiumpascode", th.StringType),
        th.Property("c_donatie", th.StringType),
    ).to_dict()


class Events(TicketmaticStream):
    """Fetches the events from Ticketmatic."""
    name = "events"
    path = "/events"
    primary_keys = ["id"]
    replication_key = "lastupdatets"

    schema = th.PropertiesList(

        th.Property("c_ticketlayoutvariant", th.StringType),
        th.Property("c_genre", th.StringType),
        th.Property("c_season", th.StringType),
        th.Property("c_hasupsells", th.StringType),
        th.Property("c_isupsellfor", th.StringType),
        th.Property("c_ypname", th.StringType),
        th.Property("c_ypid", th.StringType),
        th.Property("c_ypstartts", th.StringType),
        th.Property("c_ypendts", th.StringType),
        th.Property("c_yplocationid", th.StringType),
        th.Property("c_yplocationname", th.StringType),
        th.Property("c_ypupdatets", th.StringType),
        th.Property("c_ticketfee", th.StringType),
        th.Property("c_oldid", th.StringType),
        th.Property("c_ypaltid", th.StringType),
        th.Property("c_extratickettext", th.StringType),
        th.Property("c_noordercosts", th.StringType),
        th.Property("c_pkiid", th.StringType),
        th.Property("c_grootboekrekening", th.StringType),
        th.Property("c_vismanetcode", th.StringType),
        th.Property("c_apponly", th.StringType),
        th.Property("c_sendtofriend", th.StringType),
        th.Property("c_codedisplaybeforestart", th.StringType),
        th.Property("c_btwcode", th.StringType),
        th.Property("c_status", th.StringType),
        th.Property("c_retouroptions", th.StringType),
        th.Property("c_nohardtickets", th.StringType),


        # Ticketmatic properties
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("audiopreviewurl", th.StringType),
        th.Property(
            "availability",
            th.ArrayType(
                th.ObjectType(
                    th.Property("complimentary", th.IntegerType),
                    th.Property("free", th.IntegerType),
                    th.Property("locked_hard", th.IntegerType),
                    th.Property("locked_soft", th.IntegerType),
                    th.Property("reserved", th.IntegerType),
                    th.Property("sold_paid", th.IntegerType),
                    th.Property("sold_unpaid", th.IntegerType),
                    th.Property("tickettypeid", th.IntegerType),
                    th.Property("total", th.IntegerType),
                    th.Property("servicechargedefinitionid", th.DateTimeType),
                )
            ),
        ),
        th.Property("code", th.StringType),
        th.Property(
            "contingents",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("amount", th.IntegerType),
                    th.Property("eventid", th.IntegerType),
                    th.Property(
                        "eventspecificprices",
                        th.ObjectType(
                            th.Property("prices", th.ArrayType(
                                th.ObjectType(
                                    th.Property("pricetypeid", th.IntegerType),
                                    th.Property("availabilities",
                                                th.ArrayType(th.BooleanType)),
                                    th.Property("saleschannels",
                                                th.ArrayType(th.IntegerType)),
                                    # TODO: sometimes this returns [100,1000, null, null]. It seems to break on the nulls. Since th.NumberType cant change Nulls.
                                    # th.Property("prices", th.ArrayType(th.NumberType))
                                )
                            )),
                        ),
                    ),
                    th.Property("locks",
                                th.ArrayType(
                                    th.ObjectType(
                                        th.Property("tickettypeid", th.IntegerType),
                                        th.Property("locktypeid", th.IntegerType),
                                        th.Property("amount", th.IntegerType),
                                    )
                                )
                                ),
                    th.Property("pricelistid", th.IntegerType),
                    th.Property("withimportedbarcodes", th.BooleanType),
                )
            ),
        ),
        th.Property("currentstatus", th.IntegerType),
        th.Property("description", th.StringType),
        th.Property("endts", th.StringType),
        th.Property("externalcode", th.StringType),
        th.Property("image", th.StringType),
        th.Property("info", th.StringType),
        th.Property(
            "layout",
            th.ObjectType(
                th.Property("color", th.StringType),
                th.Property("maxImage", th.BooleanType),
            ),
        ),
        th.Property("locationid", th.IntegerType),
        th.Property("locationname", th.StringType),
        th.Property("maxnbrofticketsperbasket", th.IntegerType),
        th.Property("optinsetid", th.IntegerType),
        th.Property(
            "previews",
            th.ArrayType(
                th.ObjectType(
                    th.Property("type", th.IntegerType),
                    th.Property("url", th.StringType),
                )
            ),
        ),
        th.Property(
            "prices",
            th.ObjectType(
                th.Property(
                    "contingents", th.ArrayType(
                        th.ObjectType(
                            th.Property("contingentid", th.IntegerType),
                            th.Property("pricetypes", th.ArrayType(
                                th.ObjectType(
                                    th.Property("pricetypeid", th.IntegerType),
                                    th.Property("saleschannels", th.ArrayType(
                                        th.ObjectType(
                                            th.Property("tickettypepriceid",
                                                        th.IntegerType),
                                            th.Property("saleschannelid",
                                                        th.IntegerType),
                                            th.Property("price", th.NumberType),
                                            th.Property("servicecharge", th.NumberType),
                                            th.Property(
                                                "conditions", th.ArrayType(
                                                    th.ObjectType(
                                                        th.Property(
                                                            "type",
                                                            th.StringType,
                                                        ),
                                                        # TODO: dit kan een dicionary zijn met start / end, een array met integers of een integer lol
                                                        # th.Property(
                                                        #     "value",
                                                        #     th.ObjectType(
                                                        #         th.Property(
                                                        #             "start",
                                                        #             th.DateTimeType,
                                                        #         ),
                                                        #         th.Property(
                                                        #             "end",
                                                        #             th.DateTimeType,
                                                        #         ),
                                                        #     ),
                                                        # ),
                                                    )
                                                ),
                                            ),
                                            # No idea what this array should include
                                            th.Property(
                                                "costs", th.ArrayType(th.StringType)),
                                        )
                                    )),
                                    th.Property("price", th.NumberType),
                                    th.Property("tickettypepriceid", th.IntegerType),
                                ),
                            ),
                            ),
                        )),
                ),
            ),
        ),
        th.Property("productionid", th.IntegerType),
        th.Property("publishedts", th.DateTimeType),
        th.Property("queuetoken", th.IntegerType),
        th.Property("revenuesplitid", th.IntegerType),
        th.Property("saleendts", th.DateTimeType),
        th.Property(
            "saleschannels",
            th.ArrayType(
                th.ObjectType(
                    th.Property("eventid", th.IntegerType),
                    th.Property("haswaitinglist", th.BooleanType),
                    th.Property("isactive", th.BooleanType),
                    th.Property("saleendts", th.DateTimeType),
                    th.Property("saleschannelid", th.IntegerType),
                    th.Property("salestartts", th.StringType),
                )
            ),
        ),
        th.Property("salestartts", th.DateTimeType),
        th.Property("salestatusmessagesid", th.IntegerType),
        th.Property("schedule", th.StringType),
        th.Property("seatallowsingle", th.BooleanType),
        th.Property("seated_chartkey", th.StringType),
        th.Property(
            "seated_contingents",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("amount", th.IntegerType),
                    th.Property("eventid", th.IntegerType),
                    # No idea what to expect
                    th.Property("eventspecificprices", th.ObjectType()),
                    th.Property("locks", th.ArrayType(th.StringType)),
                    th.Property("pricelistid", th.IntegerType),
                    th.Property("withimportedbarcodes", th.BooleanType),
                )
            ),
        ),
        th.Property(
            "seatingplancontingents",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                    th.Property("amount", th.IntegerType),
                    th.Property("eventid", th.IntegerType),
                    th.Property("seatrankid", th.IntegerType),
                )
            ),
        ),
        th.Property(
            "seatingplaneventspecificprices",
            th.ObjectType(
                th.Property(
                    "prices",
                    th.ArrayType(
                        th.ObjectType(
                            th.Property("saleschannels", th.ArrayType(th.IntegerType)),
                            th.Property("prices", th.ArrayType(th.NumberType)),
                            th.Property("availabilities", th.ArrayType(th.BooleanType)),
                            th.Property("pricetypeid", th.IntegerType),
                        ),
                    ),
                ),
                th.Property("seatrankids", th.ArrayType(th.IntegerType)),

            ),
        ),
        th.Property("seatingplanid", th.IntegerType),
        th.Property("seatingplanpricelistid", th.IntegerType),
        th.Property("seatselection", th.BooleanType),
        th.Property("segmentationtags", th.ArrayType(th.StringType)),
        th.Property("servicemailids", th.ArrayType(th.IntegerType)),
        th.Property("shortdescription", th.StringType),
        th.Property("socialdistance", th.IntegerType),
        th.Property("startts", th.DateTimeType),
        th.Property("subtitle", th.StringType),
        th.Property("subtitle2", th.StringType),
        th.Property("tags", th.ArrayType(th.StringType)),
        th.Property("ticketfeeid", th.IntegerType),
        th.Property("ticketinfoid", th.IntegerType),
        th.Property("ticketlayoutid", th.IntegerType),
        th.Property("totalmaxtickets", th.IntegerType),
        th.Property(
            "translations",
            th.ObjectType(
                th.Property("nameen", th.StringType),
                th.Property("namefr", th.StringType),
            ),
        ),
        th.Property("upsellid", th.IntegerType),
        th.Property("waitinglisttype", th.IntegerType),
        th.Property("webremark", th.StringType),
        th.Property("createdts", th.DateTimeType),
        th.Property("lastupdatets", th.DateTimeType),
    ).to_dict()


class PriceTypes(TicketmaticStream):
    """
    The original/custom pricing types.
    """
    name = "price_types"
    path = "/settings/pricing/pricetypes"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("typeid", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("remark", th.StringType),
        th.Property("isarchived", th.BooleanType),
        th.Property("createdts", th.DateTimeType),
        th.Property("lastupdatets", th.DateTimeType),
    ).to_dict()

    def get_url_params(
        self,
        context: Optional[dict],
        next_page_token: Optional[Any],
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params = {
            "limit": self.limit_per_request,
            "output": "withlookup",
            "includearchived": "true",
        }

        return params


class SeatRanks(TicketmaticStream):
    """
    The original/custom seat ranks.
    """
    name = "seat_ranks"
    path = "/settings/seatingplans/seatranks"
    primary_keys = ["id"]

    schema = th.PropertiesList(
        th.Property("id", th.IntegerType),
        th.Property("name", th.StringType),
        th.Property("color", th.StringType),
        th.Property("isarchived", th.BooleanType),
        th.Property("createdts", th.DateTimeType),
        th.Property("lastupdatets", th.DateTimeType),
    ).to_dict()

    def get_url_params(
        self,
        context: Optional[dict],
        next_page_token: Optional[Any],
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params = {
            "limit": self.limit_per_request,
            "output": "withlookup",
            "includearchived": "true",
        }

        return params
