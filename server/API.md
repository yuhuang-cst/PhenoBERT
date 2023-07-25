# Data Structure
## Common Return Parameters
| Name         | Description    | Required | Type        | Notes                               |
| ------ |----------------|----------| ------ |-------------------------------------|
| version      | model version  | yes      | `string`    |                                     |
| log_id       | log id         | yes      | `string`    | debug                               |
| ret_code | status code    | yes      | `int32` | 0 means success，others means failure |
| ret_message | status message | yes      | `string` |                                     |

# PhenoBERT Phenotype Extraction
- Input single text, output hpo extraction results

## Request
- Method: `POST`
- URL: `/phenobert-input-single`

### Request Parameters
| Name | Description  | Required | Type     | Notes |
|------|--------------|----------|----------|-------|
| text | medical text | yes      | `string` |       |

## Return
### Return Parameters
| Name         | Description              | Required | Type        | Notes        |
|--------------|--------------------------|----------|-------------|--------------|
| result       | HPO extraction result    | yes      | `list`      |              |
| result.code  | linked HPO code          | yes      | `string`    |              |
| result.span  | position of mention text | yes      | `list[int]` | (start, end) |
| result.score | link score               | yes      | `float`     |              |
| result.term  | linked hpo term          | yes      | `string`    |              |
