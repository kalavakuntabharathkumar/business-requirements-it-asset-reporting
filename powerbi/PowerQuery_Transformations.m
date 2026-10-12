let
    Source = Csv.Document(
        File.Contents("C:\\PATH\\TO\\assets_120k.csv"),
        [Delimiter=",", Encoding=65001, QuoteStyle=QuoteStyle.Csv]
    ),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    TypedColumns = Table.TransformColumnTypes(PromotedHeaders,{
        {"asset_id", type text},
        {"asset_type", type text},
        {"department", type text},
        {"owner", type text},
        {"location", type text},
        {"purchase_date", type date},
        {"last_seen", type date},
        {"asset_status", type text},
        {"criticality", type text},
        {"cost", Currency.Type}
    }),
    CleanText = Table.TransformColumns(TypedColumns,{
        {"asset_type", each Text.Trim(_), type text},
        {"department", each Text.Trim(_), type text},
        {"owner", each Text.Trim(_), type text},
        {"location", each Text.Trim(_), type text},
        {"asset_status", each Text.Trim(_), type text}
    }),
    AddedDaysSinceSeen = Table.AddColumn(
        CleanText, "days_since_seen",
        each Duration.Days(Date.From(DateTime.LocalNow()) - [last_seen]),
        Int64.Type
    ),
    AddedStaleFlag = Table.AddColumn(
        AddedDaysSinceSeen, "is_stale",
        each [days_since_seen] > 30,
        type logical
    )
in
    AddedStaleFlag
