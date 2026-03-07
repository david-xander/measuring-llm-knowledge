import org.antlr.v4.runtime.*;

public abstract class RFilterBase extends Parser {
    protected int curlies = 0;

    public RFilterBase(TokenStream input) {
        super(input);
    }

    protected void hideToken(Token token) {
        if (token instanceof CommonToken) {
            ((CommonToken) token).setChannel(Token.HIDDEN_CHANNEL);
        }
    }
}